# найти ближайший индекс в списке к целевому числу
# если находим равное

NUMBERS_LIST = [1, 6, 99, 32, 54, 82, 31, 50, 48]
TARGET = 33


def nearest_index(n_list: list, target: int):
    if target in n_list:
        return n_list.index(target)
    delta = 10 ** 100
    ind_closest = None
    for ind, val in enumerate(n_list):
        temp_result = abs(val - target)
        if temp_result < delta:
            delta = temp_result
            ind_closest = ind
    return ind_closest


def nearest_index2(n_list: list, target: int):
    delta_list = [abs(val - target) for val in n_list]
    min_index = delta_list.index(min(delta_list))
    return min_index


print(nearest_index(NUMBERS_LIST, TARGET))
print(nearest_index2(NUMBERS_LIST, TARGET))
