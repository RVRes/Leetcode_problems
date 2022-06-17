from itertools import combinations


def find_three(ls: list, target: int):
    options = []
    for item in ls:
        if item <= target:
            temp_opt = []
            for option in options:
                if sum(option) + item <= target and (*option, item,) not in options:
                    temp_opt.append((*option, item,))
            if temp_opt:
                options += temp_opt
            if (item,) not in options:
                options.append((item,))

    return [item for item in options if sum(item) == target]


def get_all_combinations(arr, tgt):
    combs = [list(filter(lambda x: sum(x) == tgt, combinations(arr, i))) for i in range(len(arr)+1)]
    return [item for comb in combs for item in comb]


tests = [
    [1, 3, 5, 0, 2, 7, 10],
    [1, 0, 0, 3, 2],
    [],
    [3],
    [2, 1],
    [4, 7],
    [4]
]

target_ = 3

for test in tests:
    print(f'{test}, find_three: {find_three(test, target_)}')
    print(f'{test}, get_all_combinations: {get_all_combinations(test, target_)}')
