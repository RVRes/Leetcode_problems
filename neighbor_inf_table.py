#
# Задача №236. Бесконечная таблица
# Натуральные числа записаны в (бесконечную) таблицу, как показано на рисунке.
#
# 1
#
# Требуется по заданному числу вывести всех его соседей (числа, записанные в клетках сверху, справа, слева и снизу, если таковые имеются)
#
# Входные данные
# Вводится одно натуральное число, не превосходящее 109.
#
# Выходные данные
# Программа должна вывести все числа, записанные в соседних клетках с данным, в порядке возрастания. Числа должны разделяться пробелом.

pivot_number = int(input())  # number to find neighbors
i = -1  # increment
column_first = 1  # top number in column
while True:
    i += 2
    column_first += i
    if column_first > pivot_number:
        break
column_first -= i
i -= 2
column_number = int(i / 2 + 1.5)
column_last = column_first + i + 1  # last number in column
if pivot_number == column_first:
    neighbors = f'{(pivot_number + i + 3)}{(" " + str(pivot_number + 1)) if pivot_number + 1 < column_last else ""}'
elif pivot_number == column_last:
    neighbors = f'{(pivot_number -1)} {str(pivot_number + i+3)}'
else:
    neighbors = f'{(pivot_number -1)} {str(pivot_number + i+3)} {pivot_number - i -1} {pivot_number + 1}'
# print(neighbors)

print(
    f'neighbors = {neighbors}, pivot = {pivot_number}, column = {column_number}, column_start = {column_first}, column_last = {column_last}')
