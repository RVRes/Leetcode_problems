# напишите функцию для определения prime номеров, которые делятся на 1 и самих себя
import time
from math import sqrt


def time_of_function(function):
    def wrapped(*args):
        t1 = time.monotonic()
        t2 = time.localtime()
        res = function(*args)
        lt = str(time.strftime("%H:%M:%S", t2)) + ' ' + str("%.3f" % (time.monotonic() - t1)) + ': '
        print(lt, function.__name__, args, res)
        return res

    return wrapped


@time_of_function
def prime_numbers(limit: int) -> list:
    result = []
    for i in range(2, limit + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


# во внутреннем цикле нам не нужно делить на 4, если не получилось разделить на 2 - нужны только простые числа
@time_of_function
def prime_numbers2(limit: int) -> list:
    result = []
    for i in range(2, limit + 1):
        for j in result:
            if i % j == 0:
                break
        else:
            result.append(i)
    return result



# по теории числел, если число имеет делитель d1, то и результат деления d2 тоже может быть делителем. d1*d2 = res,
# минимальное такое число: d1=d2=sqrt(res), поэтому достаточно досчитать до квадратного корня до предполагаемого простого числа
@time_of_function
def prime_numbers3(limit: int) -> list:
    result = []
    for i in range(2, limit + 1):
        for j in result:
            if j > int(sqrt(i) + 1):
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


#  не надо проверять на числа, которые делятся на 2 (шаг) и 5(проверка), квадратный корень заменяем умножением
@time_of_function
def prime_numbers4(limit: int) -> list:
    result = [2]
    for i in range(3, limit + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in result:
            if j*j-1 > i:
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    return result



print(prime_numbers(10000))
print(prime_numbers2(10000))
print(prime_numbers3(10000))
print(prime_numbers4(10000))