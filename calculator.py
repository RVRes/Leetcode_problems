def calculator(expression: str) -> float:
    signs = '+-*/'
    try:
        sign = next(sign for sign in signs if sign in expression)
        left_value, right_value = map(int, (expression.split(sign)))
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }[sign](left_value, right_value)
    except (ValueError, TypeError, StopIteration):
        raise ValueError(f'Expression should have one of these signs: [{signs}] and two integers')


tests = [
    '10+5',
    ' 11 - 20',
    '5*  7 ',
    '300/3'
]

for test in tests:
    print(f'Expression: {test:8} , result: {calculator(test)}')

