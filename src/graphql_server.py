from src.schema import MazeSchema
import src.svg_generetor as sv

import json
from flask import Flask, render_template
from flask_cors import CORS
from flask_graphql import GraphQLView

app = Flask(__name__)
CORS(app)

schema = MazeSchema


def gen_maze():
    svg_maze = sv.Svg_Generetor("page", "False", 9, 20, "")
    print(svg_maze.file_name)
    return "/static/data/page.svg"


@app.route("/")
def index():

    return render_template('index.html', maze=json.dumps(gen_maze()))


app.add_url_rule(
    "/api", view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)
