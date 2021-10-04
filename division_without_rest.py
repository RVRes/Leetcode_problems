# def get_divident_list(result: int, divisor: int) -> list:
#     '''returns list of all possible dividents'''
#     return list(range(result * divisor, result * divisor + divisor))
#
#
# options_array = [int(input())]
# for i in range(4, 1, -1):
#     result_array = []
#     for option in options_array:
#         result_array += get_divident_list(option, i)
#     options_array = list(set(result_array))  # filtering duplicates
# print(options_array)
#



def get_divident_list(result: int, divisor: int):
    '''returns range of all possible dividents'''
    return result*divisor, result*divisor + divisor - 1


L = R = int(input())
for i in range(4, 1, -1):
    Lc = 99999999
    Rc = -1
    for option in range(L, R + 1):
        ld, rd = get_divident_list(option, i)
        if Lc > ld:
            Lc = ld
        if Rc < rd:
            Rc = rd
    L, R = Lc, Rc
options_array = ' '.join(map(str, range(L, R + 1)))
print(options_array)