# Amazon Online Assessment Questions:
#
# Robot Bounded in Box
# On an infinite plane, a robot initially stands at (0, 0) and faces north.
# The robot can receive one of three instructions:
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degrees to the right.
# The robot performs the instructions given in order, and repeats them forever.
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
# Example 1:
# Input: instructions = "GGLLGG"
# Output: true
# Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
# When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
#
# Example 2:
# Input: instructions = "GG"
# Output: false
# Explanation: The robot moves north indefinitely.
#
# Example 3:
# Input: instructions = "GL"
# Output: true
# Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
#
# Constraints:
# 1 <= instructions.length <= 100
# instructions[i] is 'G', 'L' or, 'R'.

from _tasks_runner import execute
from collections import namedtuple
from random import choice


def is_robot_movement_cycled(instructions: str) -> bool:
    turn_left = {(1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0)}
    turn_right = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
    Point = namedtuple("Point", "x y")
    position = start_position = Point(0, 0)
    direction = start_direction = Point(1, 0)
    for i in instructions:
        if i == 'G':
            position = Point(position.x + direction.x, position.y + direction.y)
        elif i == 'L':
            direction = Point(*turn_left[direction])
        else:
            direction = Point(*turn_right[direction])
    return True if position == start_position or direction != start_direction else False


TESTS = [
    [("GGLLGG",), True],
    [('GG',), False],
    [('GL',), True],
    [(''.join(choice('GLR') for _ in range(3)),), None],
    [(''.join(choice('GLR') for _ in range(4)),), None],
    [(''.join(choice('GLR') for _ in range(10)),), None]
]

for i, test in enumerate(TESTS):
    print(f'Test {i}, length {len(test[0][0])}:')
    execute(is_robot_movement_cycled, test[0], test[1], is_reference=True)

