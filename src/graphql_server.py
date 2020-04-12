import maze_generator as mz

import os
import graphene
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from graphene import Int, Float

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
CORS(app)


class MazeType(graphene.ObjectType):
    """A Simple mazetype object"""
    points = graphene.List(graphene.List(Int), description="The list of the co-ordinates of the lines to be generated")
    size = graphene.Int(description="The size of the maze")
    seed = graphene.String(description="The seed of the maze")
    color = graphene.List(graphene.List(Float), description="The list of colours of the layers Comming Soon!")
    solution = graphene.List(graphene.List(Int), description="The list of points of the solution")
    layers = graphene.Int(description="The numbers of layer of the maze")


class MazeQuery(graphene.ObjectType):
    """Various queries related to generating or retreving mazes"""
    get_maze = graphene.Field(
        MazeType,
        size=graphene.Int(description="The size of the maze to be to generated"),
        color=graphene.Boolean(description="The parameter to color the layers of the maze (comming Soon!)"),
        layer_approx=graphene.Int(description="The approximate numbers of layers for the maze to be generated"),
        seed=graphene.String(description="The Seed to generate the maze"),
        description="Generates the maze according to the size or seed"
    )

    test = graphene.String(
    )

    def resolve_test(root, info):
        return "Test Sucessful"

    def resolve_get_maze(root, info, layer_approx=1, color=False, size=1, seed=""):
        if seed != "":
            maze = mz.Maze(0, 0, seed)
        else:
            maze = mz.Maze(layer_approx, size)
        maze_package = {
            "points": maze.points,
            "solution": maze.solution,
            "layers": maze.layers,
            "size": maze.size,
            "seed": maze.seed,
            "color": maze.color
        }
        return maze_package


schema = graphene.Schema(query=MazeQuery)


@app.route("/")
def index():
    return "API endpoints available on: /api"


app.add_url_rule(
    "/api", view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
