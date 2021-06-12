# Using TypeScript if you know it, or JavaScript if you don't, write a Counter class that fulfills these requirements:
#
# - It takes an iterable of strings as an input to its constructor (e.g., `["a", "b", "a", "c"]`)
# - It provides a `count` method that takes a string as its input and returns the number of times the exact string is a value in the iterable

import random


class Counter:
    """
    returns the number of times the exact string is a value in the iterable
    """
    _str_list: list

    def __init__(self, input_list: list):
        self._str_list = input_list[::]

    def count(self, str_to_count: str) -> int:
        return self._str_list.count(str_to_count)


random_str_list = [''.join(random.choice('abcd') for _ in range(2)) for _ in range(50)]
random_str = ''.join(random.choice('abcd') for _ in range(2))

counter_1 = Counter(random_str_list)
print(counter_1.count(random_str))
