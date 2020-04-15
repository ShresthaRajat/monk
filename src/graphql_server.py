from src.schema import MazeSchema


from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

app = Flask(__name__)
CORS(app)

schema = MazeSchema


@app.route("/")
def index():
    return "<h1>Endpoints on api/</h1>"


app.add_url_rule(
    "/api", view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run()
