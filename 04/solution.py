"""Advent of Code 2015 Problem 05 Solution."""
import hashlib
import re


def __load_input(filename: str) -> str:
    """Return the first line of file called `filename`."""
    with open(filename, "r") as f:
        return f.readline().strip()


def __at_least_n_zeroes(inp: str, n: int) -> int:
    """
    Retunr the first number that produces a hash of a specified criteria.

    The hash must must start with at least n zoeroes.
    """
    i = 0
    msg_digest = ""
    pattern = f'{"0"*n}+'
    while not re.match(pattern, msg_digest):
        i += 1
        s = f"{inp}{i}"
        msg_digest = hashlib.md5(s.encode("UTF-8")).hexdigest()
    return i


def part_one_answer():
    """Return part one answer."""
    return __at_least_n_zeroes(input_str, 5)


def part_two_answer():
    """Return part two answer."""
    return __at_least_n_zeroes(input_str, 6)


input_str = __load_input("04/input/input.txt")
