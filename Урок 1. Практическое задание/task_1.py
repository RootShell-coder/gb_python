"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""

name = input('Ведите ваше имя: ')
password = input('Ведите ваш пароль: ')
age = int(input('Введите ваш возраст: '))
MSG = "Ваши данные для входа в аккаунт:"
print(f"{MSG} имя - {name}, пароль - {password}, возраст - {age}")
