# dict = {
#     'a': 100,
#     'b': 200
# }
#
# dict.get('a')
# d1_rev = dict((v, k) for k, v in d1.items())
# print(dict.values())
# print(dict.keys())
#
#
#
#
# for key, value in dict.items():
#     print (key, value)

A = [i for i in range(100)]
S = 'sample string'
D = {1: 'sadas',
     2: 'k'}

print(A.count(3))
print(A.index(3))
A.reverse()
print(A)
print(S.index('a'))
print(S.find('a'))
print(S.rfind('a'))
print(D.keys())
print(D.values())
print(list(D.items()))
print(D[1])
print([key for key, value in D.items() if value == 'k'][0])
print({value:key for key, value in D.items()}['k'])
