import src.graphql_server as gql


query = """
    {
        getMaze(size: 1, layerApprox: 10, seed: "A") {
            size
            seed
            layers
        }
    }
"""


def test_query():
    result = gql.schema.execute(query)
    assert not result.errors
    assert result.data == {
        'getMaze': {
            'size': 0,
            'seed': 'A',
            'layers': 3}
    }


test_query()
