from src.maze_generator.schema import MazeSchema
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_cors import CORS  # noqa
from flask_graphql import GraphQLView
from dotenv import load_dotenv
import src.maze_generator.maze_svg as sv
import pymongo
import bcrypt
import os
import json  # noqa

# load schema and dotenv files
schema = MazeSchema
load_dotenv()

# flask app configs
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'mongo'
app.debug = os.getenv('DEBUG')
app.secret_key = os.getenv("SECRET_KEY") or "asdasdasd"
mongouser = os.getenv("MONGO_INITDB_ROOT_USERNAME") or "root"
mongopass = os.getenv("MONGO_INITDB_ROOT_PASSWORD") or "password"
mongoip = os.getenv("MONGO_IP") or "localhost"

# mongo db configs
empty_string = "mongodb://{}:{}@{}:27017/?authMechanism=DEFAULT"
connection_string = empty_string.format(mongouser, mongopass ,mongoip)
client = pymongo.MongoClient(connection_string)
db = client["mydatabase"]


def gen_maze(size, solution=False, seed="", filename="page"):
    svg_maze = sv.Svg_generator(filename, solution, size, 60, seed)
    return svg_maze.read_svg()


@app.route("/test")
def test():
    return gen_maze(15, True)


@app.route("/")
def index():
    return render_template('index.html', maze=gen_maze(6))


@app.route("/generate", methods=['POST', 'GET'])
def generate():
    if request.method == 'POST':
        if request.form.get('solution'):
            solution = True
        else:
            solution = False
        try:
            size = int(request.form['size'])
        except ValueError:
            size = 6

        seed = request.form['seed']
        if seed:
            if not seed_check(seed):
                flash('Seed can only be combination of A, B, C and D')
                return redirect(url_for('index'))
        if size < 1:
            size = 6

        if isinstance(seed, str):
            pass
        else:
            seed = ""

        return render_template('index.html',
                               maze=gen_maze(size, solution, seed))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = client.db.users
        login_user = users.find_one({'name': request.form['username']})
        if login_user and request.form['username'] != "":
            x = request.form['pass'].encode('utf-8')
            y = login_user['password']
            z = login_user['password']
            if bcrypt.hashpw(x, y) == z:
                session['username'] = request.form['username']
                return redirect(url_for('login'))
        flash('Invalid username/password combination')
        return render_template('login.html')
    elif 'username' in session:
        return redirect(url_for('home'))
    return render_template('login.html')


@app.route('/home', methods=['GET'])
def home():
    if 'username' in session:
        maze_coll = client.db.maze
        maze_list = []
        for x in maze_coll.find():
            if x['user'] == session['username']:
                maze_list.append("static/data/" + x['seed'] + '.svg')
                gen_maze(1, False, x['seed'], x['seed'])
        return render_template('user.html', data=maze_list)
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = client.db.users
        pass1 = request.form['pass1'].encode('utf-8')
        pass2 = request.form['pass2'].encode('utf-8')
        if request.form.get('agree'):
            agree = True
        else:
            agree = False
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            if len(pass1) >= 6:
                if pass1 == pass2:
                    if agree:
                        hashpass = bcrypt.hashpw(pass1, bcrypt.gensalt())
                        users.insert({
                            'name': request.form['username'],
                            'password': hashpass
                        })
                        session['username'] = request.form['username']
                        return redirect(url_for('login'))
                    flash('You have to agree the license terms.')
                    return render_template('register.html')
                flash('Passwords do not match!')
                return render_template('register.html')
            flash('Password must be longer than 6 digits. Please use a strong password')
            return render_template('register.html')
        flash('That username already exists!')
        return render_template('register.html')
    return render_template('register.html')


def seed_check(a):
    flag = True
    for i in a:
        if i not in ["A", "B", "C", "D"]:
            flag = False
    if a == "":
        flag = False
    return (flag)


@app.route('/mazeadd', methods=['POST', 'GET'])
def mazeadd():
    if 'username' in session:
        if request.method == 'POST':
            if not request.form.get('agree'):
                flash(
                    'Download is unavailable for publishing. Please agree that you are not publishing the maze'
                )
                return redirect(url_for('login'))

            seed = request.form['seed']
            if not seed_check(seed):
                flash('Seed can only be combination of A, B, C and D')
                return redirect(url_for('login'))

            maze_coll = client.db.maze
            maze_coll.insert({'user': session['username'], 'seed': seed})
            return redirect(url_for('login'))
        else:
            flash('Adding Failed')
            return redirect(url_for('login'))
    flash('You have to register/login to proceed!.')
    return render_template('register.html')


@app.route('/mazedelete', methods=['POST', 'GET'])
def mazedelete():
    if 'username' in session:
        if request.method == 'POST':
            delete_seed = request.form['delete_seed']
            maze_coll = client.db.maze
            print(type(delete_seed))
            x = delete_seed.split("/")[2].split(".")[0]
            print(x)
            maze_coll.remove({
                'user': session['username'],
                'seed': x
            })
            # flash("Deleted "+ x)
            return redirect(url_for('login'))
        else:
            flash('Delete Failed')
            return redirect(url_for('login'))
    flash('You have to register/login to proceed!.')
    return render_template('register.html')


app.add_url_rule("/api",
                 view_func=GraphQLView.as_view("graphql",
                                               schema=schema,
                                               graphiql=True))
