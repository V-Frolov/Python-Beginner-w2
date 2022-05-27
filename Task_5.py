# Напишите программу, которая циклично запрашивает у пользователя номера
# символов по таблице Unicode и выводит соответствующие им символы.
# Завершает работу при вводе нуля.

unicodeNumber = 1
while unicodeNumber != '0':
    unicodeNumber = input('Input unicode number: ')
    print(chr(int(unicodeNumber)))

# Напишите программу, которая измеряет длину введенной строки. Если строка
# длиннее десяти символов, то выносится предупреждение. Если короче, то к
# строке добавляется столько символов *, чтобы ее длина составляла десять
# символов, после чего новая строка должна выводиться на экран.

unknownString = input('Enter string: ')
lenghtString = len(unknownString)
if lenghtString >= 10:
    print('String is to long')
else:
    unknownString = unknownString + (10 - lenghtString) * '*'
    print('Result string:', unknownString)

# Напишите программу, которая запрашивает у пользователя шесть вещественных
# чисел. На экран выводит минимальное и максимальное из них, округленные до
# двух знаков после запятой. Выполните задание без использования встроенных
# функций min() и max().

i = 1
mas = []
while i < 7:
    mas.append(float(input(f'Enter {i} real number: ')))
    i += 1
i = 0
maxNumber = minNumber = mas[0]
for i in mas:
    if maxNumber > i:
        maxNumber = i
    if minNumber < i:
        minNumber = i
print('All numbers:', mas)
print('Maximum number:', "{:.2f}".format(maxNumber))
print('Minimum number:', "{:.2f}".format(minNumber))
