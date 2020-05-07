from src.schema import MazeSchema
from flask import Flask, render_template, url_for, request, session, redirect
from flask_cors import CORS
from flask_graphql import GraphQLView
import src.svg_generetor as sv
import json
import pymongo
import bcrypt
import os


app = Flask(__name__)
CORS(app)

schema = MazeSchema

conn = os.getenv("CONN")
mongo = pymongo.MongoClient(conn)
db = mongo["mydatabase"]


def gen_maze():
    svg_maze = sv.Svg_Generetor("page", "False", 9, 20, "")
    print(svg_maze.file_name)
    return "/static/data/page.svg"


@app.route("/")
def index():
    return render_template('index.html', maze=json.dumps(gen_maze()))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})
        if login_user:
            x = request.form['pass'].encode('utf-8')
            y = login_user['password']
            z = login_user['password']
            if bcrypt.hashpw(x, y) == z:
                session['username'] = request.form['username']
                return redirect(url_for('login'))
        return 'Invalid username/password combination'
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
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            pass1 = request.form['pass1'].encode('utf-8')
            pass2 = request.form['pass2'].encode('utf-8')
            if pass1 == pass2:
                hashpass = bcrypt.hashpw(
                    pass1, bcrypt.gensalt())
                users.insert(
                    {'name': request.form['username'], 'password': hashpass})
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            return 'Passwords do not match!'

        return 'That username already exists!'

    return render_template('register.html')


app.add_url_rule(
    "/api", view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)
