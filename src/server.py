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


class maze(graphene.ObjectType):
    writtenToDb = graphene.Boolean()
    points = graphene.List(graphene.List(Int))
    size = graphene.Int()
    seed = graphene.String()
    color = graphene.List(graphene.List(Float))
    solution = graphene.List(graphene.List(Int))
    layers = graphene.Int()
    layers_approx = graphene.Int()


class Query(graphene.ObjectType):

    get_maze = graphene.Field(
        maze,
        size=graphene.Int(),
        color=graphene.Boolean(),
        layer_approx=graphene.Int()
    )

    test = graphene.String(
    )

    def resolve_test(root, info):
        return "Test Sucessful"

    def resolve_get_maze(root, info, layer_approx=1, color=False, size=1):
        writtenToDb = False
        maze = mz.Maze(layer_approx, size)
        maze_package = {
            "writtenToDb": writtenToDb,
            "points": maze.points,
            "solution": maze.solution,
            "layers": maze.layers,
            "layers_approx": maze.layers,
            "size": maze.size,
            "seed": maze.seed,
            "color": maze.color

        }
        return maze_package


schema = graphene.Schema(query=Query)


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
