"""Advent of Code 2015 Code Solution."""

def _load_floor_seq(file: str) -> str:
    """Return only the first line of `file`, without any whitespace."""
    with open(file, 'r') as f:
        return f.readline().strip()

def _get_floor(floor_dir_seq: str) -> int:
    """
    Return the final floor after simulating the floor sequence.
    
    Simulation is uses `floor_dir_seq`, where a '(' means going up one floor,
    and ')' means going down one floor. The simulation starts at floor 0.
    """
    up_count = floor_dir_seq.count('(')
    dn_count = floor_dir_seq.count(')')
    return up_count-dn_count

def _basement_first_occ(floor_dir_seq: str) -> int:
    """
    Return the index of the first char that brings Santa to the basement.
    
    The first char is defined as the first character in `floor_dir_seq`, where
    '(' means going up one floor, and ')' means going down one floor. The
    simulation starts at floor 0. Also, the index returned is 1-index based.
    """
    current_floor: int = 0
    index: int
    for i, c in enumerate(floor_dir_seq):
        current_floor += 1 if c == '(' else -1
        if current_floor == -1:
            index = i + 1
            break
    return index

def part_one_answer() -> int:
    """Return part one answer."""
    return _get_floor(floor_seq)

def part_two_answer() -> int:
    """Return part two answer."""
    return _basement_first_occ(floor_seq)

floor_seq = _load_floor_seq('01/input/input.txt')