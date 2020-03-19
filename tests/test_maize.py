import src.maze as maze
import pytest  # noqa


def test_draw_random_check_maize_part():
    sample = maze.Maze()
    output = sample.draw_random()
    assert isinstance(output[0], list)


def test_draw_random_check_maize_solution():
    sample = maze.Maze()
    output = sample.draw_random()
    assert isinstance(output[4], list)


def test_draw_random_maze_validity_check():
    sample = maze.Maze()
    output = sample.draw_random()
    points = output[0]
    assert len(points) > 1


def test_draw_random_solution_validity_check():
    sample = maze.Maze()
    output = sample.draw_random()
    solution = output[4]
    assert len(solution) > 1


# def test_genc_coordinates_is_number_pairs():
#     output = m.genc(10)
#     random_coordinates = random.choice(output)
#     assert len(random_coordinates) == 2


# def test_genc_coordinates_is_number_pairs_int():
#     output = m.genc(10)
#     random_coordinates = random.choice(output)
#     assert isinstance(type(random_coordinates[0], int)


# def test_genc_coordinates_is_number_pairs_int_second_digit():
#     output=m.genc(10)
#     random_coordinates=random.choice(output)
#     assert isinstance(type(random_coordinates[1]), int)
