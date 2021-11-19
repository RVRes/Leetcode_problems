# переводим из одной системы исчисления в любую другую
from string import ascii_lowercase


def dec_to_letter(num: int) -> str:
    return ascii_lowercase[num - 10] if 9 < num <= 36 else None


def letter_to_dec(letter: str) -> int:
    return 10 + ascii_lowercase.find(letter) if letter in ascii_lowercase else None


def convert_to_decimal(num_string: str, base_from: int) -> int:
    is_negative = False
    if num_string[0] == '-':
        is_negative = True
        num_string = num_string[1::]
    num_string = num_string[::-1]
    result = 0
    for pos, char in enumerate(num_string):
        char = letter_to_dec(char) if char in ascii_lowercase else int(char)
        result += char * (base_from ** pos)
    return result if not is_negative else -1 * result


def convert_from_decimal(num_string: str, base_to: int) -> str:
    is_negative = False
    if num_string[0] == '-':
        is_negative = True
        num_string = num_string[1::]
    num = int(num_string)
    result = []
    while num >= base_to:
        result.append(num - num // base_to * base_to)
        num = num // base_to
    result.append(num)
    result = result[::-1]
    result = ''.join(map(str, map(lambda x: x if x < 10 else dec_to_letter(x), result)))
    return result if not is_negative else -1 * result


def convert(num_str: str, base_from: int, base_to: int) -> str:
    return convert_from_decimal(str(convert_to_decimal(num_str, base_from)), base_to)


print(convert('1010101011110000100000', 10, 11))
