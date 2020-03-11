import src.Maze as m
import pytest  # !NOUIC
import random


def test_draw_random_check_maize_part():
    output = m.draw_random(10)
    assert type(output[0]) == type([])


def test_draw_random_check_maize_solution():
    output = m.draw_random(10)
    assert type(output[4]) == type([])


def test_draw_random_maze_validity_check():
    output = m.draw_random(10)
    maze = output[0]
    assert len(maze) > 1


def test_draw_random_solution_validity_check():
    output = m.draw_random(10)
    solution = output[4]
    assert len(solution) > 1


def test_genc_coordinates_is_number_pairs():
    output = m.genc(10)
    random_coordinates = random.choice(output)
    assert len(random_coordinates) == 2


def test_genc_coordinates_is_number_pairs_int():
    output = m.genc(10)
    random_coordinates = random.choice(output)
    assert (type(random_coordinates[0]) == type(1))


def test_genc_coordinates_is_number_pairs_int_second_digit():
    output = m.genc(10)
    random_coordinates = random.choice(output)
    assert (type(random_coordinates[1]) == type(1))
