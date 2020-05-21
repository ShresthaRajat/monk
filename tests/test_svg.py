import pytest  # noqa
from os import listdir, remove
import src.maze_generetor.maze_svg as svg


def test_create_svg():
    svg.Svg_Generetor("test", True, 3, 12, "")
    assert ("test.svg" in listdir("./src/static/data"))


def test_create_svg_with_solution():
    svg.Svg_Generetor("solution", True, 3, 12, "")
    assert ("solution.svg" in listdir("./src/static/data"))


def test_read_svg():
    x = svg.Svg_Generetor("solution", True, 3, 12, "")
    assert x.read_svg()


def test_clear_files():
    test_files = (
        "test.svg" in listdir("./src/static/data")
        and "solution.svg" in listdir("./src/static/data")
    )
    remove("./src/static/data/test.svg")
    remove("./src/static/data/solution.svg")
    assert test_files
