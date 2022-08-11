"""Advent of Code 2015 Problem 02 Code Solution."""

from collections import namedtuple
from typing import List
from functools import reduce

Dimensions = namedtuple("Dimensions", "l w h")

def __surface_area(box: Dimensions) -> int:
    """Return the surface area of `box`."""
    l, w, h = box
    return 2*l*w + 2*w*h + 2*h*l

def __cubic_volume(box: Dimensions) -> int:
    """Return the cubic volume of `box`."""
    l, w, h = box
    return l*w*h

def __smallest_perimeter(box: Dimensions) -> int:
    """Return the smallest perimeter of any one side of `box`."""
    fst, snd = sorted(box)[:2]
    return 2*fst + 2*snd

def __smallest_area(box: Dimensions) -> int:
    """Return the smallest area of any one side of `box`."""
    fst, snd = sorted(box)[:2]
    return fst*snd

def __calculate_needed_wrapping_paper(boxes: List[Dimensions]) -> int:
    """
    Return the total wrapping paper needed for each box.
    
    The total wrapping paper needed for one box is its surface area plus the
    area of its smallest side.
    """
    return reduce(lambda p, b: p + __surface_area(b) + __smallest_area(b), boxes, 0)

def __calculate_needed_ribbon(boxes: List[Dimensions]) -> int:
    """
    Return the total ribbon needed for each box.

    The total ribbon needed for a box is the sum of the cubic volume plus the
    smallest perimeter of any one side.
    """
    return reduce(lambda p, b: p + __cubic_volume(b) + __smallest_perimeter(b), boxes, 0)

def __load_dimensions(file: str) -> List[Dimensions]:
    """Return all the dimensions specified in `file`."""
    dimensions: List[Dimensions] = []

    with open(file, 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            l, w, h = [int(v) for v in line.split('x')]
            dimensions.append(Dimensions(l, w, h))

    return dimensions

def part_one_answer() -> int:
    """Return part one answer."""
    return __calculate_needed_wrapping_paper(box_list)

def part_two_answer() -> int:
    """Return part two answer."""
    return __calculate_needed_ribbon(box_list)

box_list = __load_dimensions('02/input/input.txt')