# проверить строку со скобками, что расположены в правильном порядке (открывающая - закрывающая)
# используем стек,тк мы не должны пропускать пересечения скобок. в конце проверям, что стек пустой - скобки закрыты


from queue import LifoQueue

INPUT_STRING = ']'


# def string_validation(in_str: str):
#     BRACKETS_MAPPING = {
#         '{': '}',
#         '[': ']',
#         '(': ')'}
#     stack = LifoQueue()
#     for symbol in in_str:
#         if symbol in BRACKETS_MAPPING.keys():
#             stack.put(symbol)
#         else:
#             prev_bracket = stack.get()
#             if BRACKETS_MAPPING[prev_bracket] != symbol:
#                 return False
#     if not stack.empty():
#         return False
#     return True
#
#
# print(string_validation(INPUT_STRING))


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}
        stack = LifoQueue()
        for l in s:
            if l in bracket_pairs:
                stack.put(l)
            elif stack.empty() or bracket_pairs[stack.get()] != l:
                return False
        return True if stack.empty() else False


s = Solution()
print(s.isValid(INPUT_STRING))
