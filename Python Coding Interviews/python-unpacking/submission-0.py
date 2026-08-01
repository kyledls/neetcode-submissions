from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    x1, y1, z1 = triplet[0], triplet[1], triplet[2]
    sum_3 = triplet[0] + triplet[1] + triplet[2]
    return sum_3


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    x1, y1, z1 = box_dimensions[0], box_dimensions[1], box_dimensions[2]
    volume = box_dimensions[0] * box_dimensions[1] * box_dimensions[2]
    return volume

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
