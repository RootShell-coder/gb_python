"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников
и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

person = {}
with open('my_file.txt', 'r', encoding="utf-8") as file:
    for el in file:
        person[el.split()[0]] = float(el.split()[1])

# print(person)
print("Сотрудники получающие меньше 20000: ")
for n, i in person.items():
    if i < 20_000:
        print(f"{n} {i}")

print(f"Средняя зарплата: {sum(person.values()) / len(person):.2f}")
