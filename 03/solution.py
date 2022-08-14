"""Advent of Code 2015 Problem 03 Solution."""


from collections import namedtuple
from typing import Set

Coordinate = namedtuple("Coordinate", "x y")


def __load_moves(file: str) -> str:
    """
    Return the sequence of moves from `file` as a string.

    Each move is a single character: ^,v,>, and <.
    """
    with open(file, "r") as f:
        return f.readline().strip()


def __simulate_moves(moves: str) -> int:
    """
    Simulate the sequence of moves in `moves`.

    Here is what each move does:
        ^ - north
        > - east
        v - south
        < - west

    Return the number of unique positions.
    """
    current_position = Coordinate(0, 0)

    positions_visited: Set[Coordinate] = {current_position}

    for move in moves:
        x, y = current_position
        match move:
            case "^":
                y += 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "<":
                x -= 1
        new_position = Coordinate(x, y)
        positions_visited.add(new_position)
        current_position = new_position
    return len(positions_visited)


def __simulate_moves_with_robo_santa(moves: str) -> int:
    """
    Simulate the sequence of moves in `moves` with two movers.

    The movers will alternate moves, each recording their own current position
    for each move the make.
    Here is what each move does:
        ^ - north
        > - east
        v - south
        < - west

    Return the number of unique positions among both movers.
    """
    current_position = Coordinate(0, 0)
    other_position = Coordinate(0, 0)

    positions_visited: Set[Coordinate] = {current_position, other_position}

    for move in moves:
        x, y = current_position
        match move:
            case "^":
                y += 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "<":
                x -= 1
        new_position = Coordinate(x, y)
        positions_visited.add(new_position)
        current_position = other_position
        other_position = new_position
    return len(positions_visited)


def part_one_answer() -> int:
    """Return part one answer."""
    return __simulate_moves(moves)


def part_two_answer() -> int:
    """Return part two answer."""
    return __simulate_moves_with_robo_santa(moves)


moves = __load_moves("03/input/input.txt")
