import src.maze_generator as mz
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
    sample = mz.Maze(4,
                     4)
    sample.generate()
    assert sample.size > 0
