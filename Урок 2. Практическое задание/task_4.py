"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

words = input("Введите слова через пробел: ").split()
for i, el in enumerate(words):
    print(f"{i + 1}. {el if len(el) <= 10 else el[:10]}")
