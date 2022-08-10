"""Advent of Code 2015 Code Solution."""

def _load_floor_seq(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.readline().strip()

def _get_floor(floor_dir_seq: str) -> int:
    up_count = floor_dir_seq.count('(')
    dn_count = floor_dir_seq.count(')')
    return up_count-dn_count


def part_one_answer() -> int:
    """Return part one answer."""
    return _get_floor(floor_seq)

def part_two_answer() -> int:
    pass

floor_seq = _load_floor_seq('01/input/input.txt')
print(part_one_answer())