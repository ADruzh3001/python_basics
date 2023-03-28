""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def func_division (*args):
    try:
        args_1 = float(input("Введите первое число: "))
        args_2 = float(input("Введите второе число: "))
        r = args_1 / args_2
    except BaseException:
        print("Ошибка: Введите корректное число!")

    return round(r, 2)

print(func_division())



"""def division (*args):
    try:
        args1 = int(input("Input args1: "))
        args2 = int(input("Input args2: "))
        res = args1 / args2
    except BaseException:
        return ("ERROR. EXIT.")
        exit(-1)

    return int(res)

print(division())"""
