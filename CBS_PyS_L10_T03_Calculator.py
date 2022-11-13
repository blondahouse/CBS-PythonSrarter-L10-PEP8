import math


def my_menu(list_items):
    for index, value in enumerate(list_items):
        print(f'\t{index + 1}. {value}')
    print(f'\t0. Exit\n')


def dialogue(message, list_length):
    while True:
        input_string = input(message)
        try:
            range(list_length + 1).index(int(input_string))
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(input_string)


def int_non_negative(message):
    while True:
        input_string = input(message)
        try:
            if int(input_string) <= 0:
                raise ValueError
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return int(input_string)


def float_non_one(message):
    while True:
        input_string = input(message)
        try:
            if float(input_string) == 1:
                raise ValueError
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(input_string)


def float_non_pi_n(message):
    while True:
        input_string = input(message)
        try:
            if not float(input_string) % math.pi:
                raise ValueError
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(input_string)


def float_any(message):
    while True:
        input_string = input(message)
        try:
            float(input_string)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(input_string)


def float_non_zero(message):
    while True:
        input_string = input(message)
        try:
            1 / float(input_string)
        except ValueError:
            print("\t\tError message: Wrong input, try again")
        else:
            return float(input_string)


def my_sum():
    first_term = float_any('\tEnter first term (any float number): ')
    second_term = float_any('\tEnter second term (any float number): ')
    print(f'\t\t{first_term} + {second_term} = {[first_term + second_term]}\n')


def my_dif():
    first_term = float_any('\tEnter first term (any float number): ')
    second_term = float_any('\tEnter second term (any float number): ')
    print(f'\t\t{first_term} - {second_term} = {first_term - second_term}\n')


def my_mul():
    first_factor = float_any('\tEnter first factor (any float number): ')
    second_factor = float_any('\tEnter second factor (any float number): ')
    print(f'\t\t{first_factor} * {second_factor} = {first_factor * second_factor}\n')


def my_div():
    dividend = float_any('\tEnter dividend (any float number): ')
    divisor = float_non_zero('\tEnter divisor (non zero float number): ')
    print(f'\t\t{dividend} / {divisor} = {dividend / divisor}\n')


def my_fac():
    number = int_non_negative('\tEnter non negative integer: ')
    print(f'\t\t{number}! = {math.factorial(number)}')


def my_pow():
    base = float_any('\tEnter base (any float number): ')
    exponent = float_any('\tEnter exponent (any float number): ')
    print(f'\t\t{base} ^ {exponent} = {math.pow(base, exponent)}\n')


def my_log():
    base = float_non_one('\tEnter base (float number non equal to one): ')
    anti_logarithm = float_any('\tEnter anti-logarithm (any float number): ')
    print(f'\t\tlog {base} ({anti_logarithm}) = {math.log(anti_logarithm, base)}\n')


def my_sin():
    angle_in_radians = float_any('\tEnter angle in radians (any float number): ')
    print(f'\t\tsin({angle_in_radians}) = {math.sin(angle_in_radians)}\n')


def my_cos():
    angle_in_radians = float_any('\tEnter angle in radians (any float number): ')
    print(f'\t\tcos({angle_in_radians}) = {math.cos(angle_in_radians)}\n')


def my_tan():
    angle_in_radians = float_any('\tEnter angle in radians (any float number): ')
    print(f'\t\ttan({angle_in_radians}) = {math.tan(angle_in_radians)}\n')


def my_ctg():
    angle_in_radians = float_non_pi_n('\tEnter angle in radians (float number non equal to pi * n): ')
    print(f'\t\tlog({angle_in_radians}) = {1 / math.tan(angle_in_radians)}\n')


operation_list = ['sum',
                  'dif',
                  'mul',
                  'div',
                  'fac',
                  'pow',
                  'log',
                  'sin',
                  'cos',
                  'tan',
                  'ctg']

stop_sign = 1
while stop_sign:
    my_menu(operation_list)
    stop_sign = dialogue('\tEnter action number (integer): ', len(operation_list))
    match stop_sign:
        case 1:  # sum
            my_sum()
        case 2:  # dif
            my_dif()
        case 3:  # mul
            my_mul()
        case 4:  # div
            my_div()
        case 5:  # fac
            my_fac()
        case 6:  # pow
            my_pow()
        case 7:  # log
            my_log()
        case 8:  # log
            my_sin()
        case 9:  # log
            my_cos()
        case 10:  # log
            my_tan()
        case 11:  # log
            my_ctg()
