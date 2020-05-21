import src.maze_generetor.maze as mz
import pytest  # noqa


def test_draw_random_check_maize_part():
    sample = mz.Maze()
    output = sample.draw_random()
    assert isinstance(output[0], list)


def test_draw_random_check_maize_solution():
    sample = mz.Maze()
    output = sample.draw_random()
    assert isinstance(output[4], list)


def test_draw_random_maze_validity_check():
    sample = mz.Maze()
    output = sample.draw_random()
    points = output[0]
    assert len(points) > 1


def test_draw_random_solution_validity_check():
    sample = mz.Maze()
    output = sample.draw_random()
    solution = output[4]
    assert len(solution) > 1


def test_generate_maze():
    sample = mz.Maze(4, 4)
    sample.generate()
    assert sample.size > 0


def test_generate_maze_seed():
    sample = mz.Maze(0, 0, "AAA")
    sample.generate()
    assert sample.seed == "AAA"


def test_draw_layer():
    sample = mz.Maze()
    output = sample.draw_layer("A")
    layer = output[2]
    assert layer == "A"


def test_layer_break():
    sample = mz.Maze(10, 10, "AAA")
    sample.generate()
    assert sample.seed == "AAA"
