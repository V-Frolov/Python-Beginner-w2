# В программировании можно из одной функции вызывать другую. Для иллюстрации
# этой возможности напишите программу по следующему описанию.
#
# Основная ветка программы, не считая заголовков функций, состоит из одной
# строки кода. Это вызов функции test(). В ней запрашивается на ввод целое число.
# Если оно положительное, то вызывается функция positive(), тело которой содержит
# команду вывода на экран слова "Положительное". Если число отрицательное, то
# вызывается функция negative(), ее тело содержит выражение вывода на экран слова
# "Отрицательное".
#
# Понятно, что вызов test() должен следовать после определения функций.
# Однако имеет ли значение порядок определения самих функций? То есть должны ли
# определения positive() и negative() предшествовать test() или могут следовать
# после него? Проверьте вашу гипотезу, поменяв объявления функций местами.
#
# Попробуйте объяснить результат добавив комментарии к коду.


def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    unknownNumber = 1
    while unknownNumber != 0:
        unknownNumber = input("Input integer number: ").strip()
        if (unknownNumber[0] == '-') and (unknownNumber[1:].isdecimal()):
            unknownNumber = int(unknownNumber)
            break
        else:
            unknownNumber = int(unknownNumber)
            break
    if unknownNumber > 0:
        positive()
    elif unknownNumber < 0:
        negative()
    else:
        print("Number it's 0")


test()

# Важно, чтобы функции были определены перед использованием. Очерёдность значения не имеет.