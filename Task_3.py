# Напишите программу, в которой вызывается функция, запрашивающая с ввода две
# строки и возвращающая в программу результат их конкатенации.
#
# Выведите результат на экран.


def concatStr():
    first_string = input("Input first string: ")
    second_string = input("Input second string: ")
    return first_string + second_string


print('Concatenated string: ', concatStr())


# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до
# тех пор, пока не будет введен 0. Функция должна возвращать полученное
# произведение. Вызовите функцию и выведите на экран результат ее работы.

def multiplicationNumbers():
    firstNumber = input("Input first number: ")
    if firstNumber.isdecimal():
        firstNumber = int(firstNumber)
    else:
        firstNumber = 1
    multiplicationNumber = input("Input second number: ")
    if multiplicationNumber.isdecimal():
        multiplicationNumber = int(multiplicationNumber)
    else:
        multiplicationNumber = 1
    while (firstNumber != 0) or (firstNumber is str):
        multiplicationNumber = multiplicationNumber * firstNumber
        print('Result multiplication:', multiplicationNumber)
        firstNumber = input("Input next number: ")
        if firstNumber.isdecimal():
            firstNumber = int(firstNumber)
        else:
            firstNumber = 1
    return multiplicationNumber


print(multiplicationNumbers())
