from src.schema import MazeSchema
from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_cors import CORS  # noqa
from flask_graphql import GraphQLView
from dotenv import load_dotenv
import src.svg_generetor as sv
import pymongo
import bcrypt
import os

# load schema and dotenv files
schema = MazeSchema
load_dotenv()

# flask app configs
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'mongo'
app.debug = os.getenv('DEBUG')
app.secret_key = os.getenv("SECRET_KEY")

# mongo db configs
client = pymongo.MongoClient(os.getenv("MONGO_MAZER_KEY"))
db = client["mydatabase"]


def gen_maze(size, solution=False, seed=""):
    svg_maze = sv.Svg_Generetor("page", solution, size, 60, seed)
    return svg_maze.read_svg()


@app.route("/test")
def test():
    return gen_maze(15, True)


@app.route("/")
def index():
    return render_template('index.html', maze=gen_maze(4))


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
            size = 4

        seed = request.form['seed']
        if size < 1:
            size = 4

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
        if login_user:
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
        return render_template('user.html')
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
        print(agree)
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:

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
        flash('That username already exists!')
        return render_template('register.html')

    return render_template('register.html')


app.add_url_rule("/api",
                 view_func=GraphQLView.as_view("graphql",
                                               schema=schema,
                                               graphiql=True))
