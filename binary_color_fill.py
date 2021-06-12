# представим, что вам надо залить картинку цветом, цвета обозначаются числами в картинке, к соседнему
# цвету заливка может попасть только по вертикали или горизонтали, напишите процедуру.

import random
from pprint import pprint

random.seed('234')
N = 10
pattern = [
    [random.randint(0, 9) if random.randint(0, 9) > 5 else 0 for _ in range(N)] for _ in range(N)
]
pprint(pattern)


def binary_color_fill(pattern: list, col: int, row: int, new_color: int):
    c, r = col - 1, row - 1
    c_max, r_max = len(pattern) - 1, len(pattern[0]) - 1

    old_color = pattern[c][r]
    pattern[c][r] = new_color
    if c > 0 and pattern[c - 1][r] == old_color: pattern = binary_color_fill(pattern, col - 1, row, new_color)
    if c < c_max and pattern[c + 1][r] == old_color: pattern = binary_color_fill(pattern, col + 1, row, new_color)
    if r > 0 and pattern[c][r - 1] == old_color: pattern = binary_color_fill(pattern, col, row - 1, new_color)
    if r < r_max and pattern[c][r + 1] == old_color: pattern = binary_color_fill(pattern, col, row + 1, new_color)
    return pattern

pprint(binary_color_fill(pattern, 5, 6, 99))
