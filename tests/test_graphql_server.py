import src.graphql_server as gql

maze_query = """
    {
        getMaze(size: 1, layerApprox: 10, seed: "A") {
            size
            seed
            layers
        }
    }
"""

maze_query_2 = """
    {
        getMaze(size: 1, layerApprox: 10, seed: "") {
            size
        }
    }
"""

svg_query = """
    {
        getSvg(seed: "A") {
            seed
        }
    }

"""

svg_query_2 = """
    {
        getSvg(seed: "") {
            size
        }
    }

"""


def test_maze_query_errors():
    result = gql.schema.execute(maze_query)
    assert not result.errors


def test_maze_query_2():
    result = gql.schema.execute(maze_query_2)
    assert result.data == {"getMaze": {"size": 1}}


def test_maze_query():
    result = gql.schema.execute(maze_query)
    assert result.data == {'getMaze': {'size': 0, 'seed': 'A', 'layers': 3}}


def test_svg_query_errors():
    result = gql.schema.execute(svg_query)
    assert not result.errors


def test_svg_query():
    result = gql.schema.execute(svg_query)
    assert result.data == {"getSvg": {"seed": "A"}}


def test_svg_query_2():
    result = gql.schema.execute(svg_query_2)
    assert result.data == {"getSvg": {"size": 7}}


def test_gen_maze():
    assert gql.gen_maze(1)
