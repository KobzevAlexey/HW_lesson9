from fractions import Fraction as F


def calc_fraction_main(string):
    a, move, b = string.split()

    from datetime import datetime
    from fractions import Fraction as F
    if move == '+':
        result = F(a) + F(b)
    elif move == '-':
        result = F(a) - F(b)
    elif move == '*':
        result = F(a) * F(b)
    elif move == '/':
        result = F(a) / F(b)
    else:
        return 'вы ввели некорректные данные'
    with open('log_calc.txt', 'a') as output_file:
        data = datetime.now().strftime('%Y.%m.%d %H:%M:%S  ')
        output_file.writelines(f'{data} {a} {move} {b} = {result}\n')
    return f'результат равен {result}'
