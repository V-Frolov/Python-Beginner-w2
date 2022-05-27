# Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах
# (1а, 1б, 2б, 6а, 7в и т. п.)
school = dict(c1a=7, c1b=8, c2b=5, c6a=10, c7v=9)

print('Number of students in the each class:', school)

# Внесите изменения в словарь согласно следующему:

# а) в одном из классов изменилось количество учащихся
school['c1a'] = 12

# б) в школе появился новый класс(добавьте новый клас)
school['c7a'] = 11

# с) в школе был расформирован (удален) другой класс
school.pop('c1b')

# Вычислите и выведите общее количество учащихся в школе
count = 0
for oneClass in school.values():
    count += oneClass
print('Number of students in the school:', count)
print('Number of students in the each class:', school)


# Напишите функцию, которая принимает один словарь, и возвращает другой,
# в котором ключами являются значения из первого словаря, а значениями –
# соответствующие им ключи. Создайте словарь, передайте его в функцию.
# Выведите на экран исходный и "перевернутый" словари.

def reverseDict(sourceDict):
    destinationDict = {}
    for key, value in sourceDict.items():
        destinationDict[value] = key
    return destinationDict


reversedDict = reverseDict(school)
print('Reversed dictionary:', reversedDict)
