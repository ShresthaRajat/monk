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

svg_query = """
    {
        getSvg(seed: "A") {
            seed
        }
    }

"""


def test_maze_query():
    result = gql.schema.execute(maze_query)
    assert not result.errors
    assert result.data == {
        'getMaze': {
            'size': 0,
            'seed': 'A',
            'layers': 3}
    }


def test_svg_query():
    result = gql.schema.execute(svg_query)
    assert not result.errors
    assert result.data == {
            "getSvg": {
                "seed": "A"
            }
        }


def test_gen_maze():
    assert gql.gen_maze()
