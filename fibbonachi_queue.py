# Вернуть элемент последовательнсоти фиббоначи
# Ряд чисел Фибоначчи представляет собой последовательность.
# Первый и второй элементы последовательности равны единице.
# Каждый последующий элемент равен сумме двух предыдущих.
# Рассмотрим разные способы нахождения элементов по номеру и генерацию списка с помощью Python 3.
# (иногда начинают с 0) 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
import math
import time


def time_of_function(function):
    def wrapped(*args):
        t1 = time.monotonic()
        t2 = time.localtime()
        res = function(*args)
        lt = str(time.strftime("%H:%M:%S", t2)) + ' ' + str("%.3f" % (time.monotonic() - t1)) + ': '
        lt += ' ' * (20 - len(lt))
        # print(lt, function.__name__, args, res)
        f_name = function.__name__
        f_name += ' ' * (20 - len(f_name))
        print(lt, f_name, args, res)
        return res

    return wrapped


def fibonacci1(n: int) -> int:
    prv = cur = 1
    for i in range(n - 1):
        cur = prv + cur
        prv = cur - prv
    return cur


def fibonacci2(n: int) -> int:
    prv = cur = 1
    for _ in range(n - 2):
        prv, cur = cur, prv + cur
    return cur


def fibonacci3(n):
    cur = 1
    if n > 1:
        cur = fibonacci3(n - 1) + fibonacci3(n - 2)
    return cur


#рекурсия в 1 строку через lambda функцию
fibonacci3_1 = lambda n: fibonacci3_1(n - 1) + fibonacci3_1(n - 2) if n > 1 else 1



# #генератор списка
# def fibonacci(n):
#     a, b = 1, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# data = list(fibonacci(10))
#
#
# #генератор последовательности
# def fibonacci():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# gen = fibonacci()
# for i in range(5):
#     print(next(gen))

def fibonacci4(n):
    SQRT5 = math.sqrt(5)
    PHI = (SQRT5 + 1) / 2
    return int(PHI ** (n+1) / SQRT5 + 0.5)



L = []
for i in range(10):
    L.append(fibonacci1(i))
print(L)


n=5
print(fibonacci1(n), fibonacci2(n), fibonacci3(n), fibonacci3_1(n), fibonacci4(n))
