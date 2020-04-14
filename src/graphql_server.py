from src.schema import MazeType, MazeQuery, MazeSchema


from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

app = Flask(__name__)
app.debug = True
CORS(app)

schema = MazeSchema


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
