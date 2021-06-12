import time, random


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
        print(lt, 'OK    ' if res == sorted(arg) else 'ERROR!', f_name, '  ', res[0:50:])
        return res

    return wrapped


@time_of_function
def bubble_sort(L: list) -> list:
    L = L[::]
    len_l = len(L)
    is_done = False
    for j in range(len_l, 0, -1):
        if is_done:
            break
        is_done = True
        for i in range(j - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                is_done = False
    return L


@time_of_function
def shaker_sort(L: list) -> list:
    L = L[::]
    left = 0
    right = len(L)
    is_done = False
    while not is_done:
        is_done = True
        for i in range(right - 1):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                is_done = False
        right -= 1
        if is_done:
            break
        is_done = True
        for i in range(right, left + 1, -1):
            if L[i] < L[i - 1]:
                L[i], L[i - 1] = L[i - 1], L[i]
                is_done = False
        left += 1
    return L


@time_of_function
def comb_sort(L: list) -> list:
    L = L[::]
    gap = len_l = len(L)
    is_done = False
    while not is_done or gap > 1:
        gap = max(1, int(gap / 1.24))
        is_done = True
        for i in range(len_l - gap):
            if L[i] > L[i + gap]:
                L[i], L[i + gap] = L[i + gap], L[i]
                is_done = False
    return L


@time_of_function
def quick_sort_func(L: list) -> list:
    def _quick_sort_func(L: list):
        if len(L) <= 1:
            return L
        # q = random.choice(L)
        q = L[len(L)//2]
        left = [n for n in L if n < q]
        middle = [q] * L.count(q)
        right = [n for n in L if n > q]
        return _quick_sort_func(left) + middle + _quick_sort_func(right)

    L = L[::]
    return _quick_sort_func(L)


@time_of_function
def quick_sort(L: list) -> list:
    fst = 0
    lst = len(L) - 1
    L = L[::]

    def _quick_sort(L: list, fst: int, lst: int):
        if fst >= lst: return
        left, right = fst, lst
        pivot = L[random.randint(fst, lst)]
        while left <= right:
            while L[left] < pivot: left += 1
            while L[right] > pivot: right -= 1
            if left <= right:
                L[left], L[right] = L[right], L[left]
                left += 1
                right -= 1
        # print(pivot,L[fst:lst+1:], L[fst:right+1:], L[left:lst+1:])
        _quick_sort(L, fst, right)
        _quick_sort(L, left, lst)

    _quick_sort(L, fst, lst)
    return L


@time_of_function
def python_sort(L: list):
    L.sort()
    return L


random.seed(3452345)
test_tasks = {
    1: [],
    2: [0],
    3: [-100],
    4: [1, 2, 3, 4, 5, 6, 0],
    5: [10, 7, 5, 1, 2, 0, -10, 20],
    6: [random.randint(-100, 100) for _ in range(1000)],
    7: [random.randint(-1000, 1000) for _ in range(5000)],
    8: [random.randint(-100000, 100000) for _ in range(10000)],
    # 9: [random.randint(-1000000, 1000000) for _ in range(1000000)]
}
for test_num, arg in test_tasks.items():
    print()
    print('Test', test_num, arg if len(arg) < 100 else f'[len = {len(arg)}]')
    bubble_sort(arg)
    shaker_sort(arg)
    comb_sort(arg)
    quick_sort_func(arg)
    quick_sort(arg)
    python_sort(arg)
