from flask import Flask
import graphene
import os
from graphene import ObjectType, String, Schema, Boolean, List, Int
from flask_graphql import GraphQLView
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.debug = True
CORS(app)


class Maze(ObjectType):
    hashId = Int()
    writtenToDb = Boolean()
    points = List(List(Int))

class Query(ObjectType):

    get_maze = graphene.Field(Maze)

    test = String(
    )

    def resolve_test(root, info):
        return "Test Sucessful"

    def resolve_get_maze(root, info):
        maze = {"hashId":1, "writtenToDb": False, "points": [[1,2],[2,3],[3,4]]}
        return maze


schema = Schema(query=Query)


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
