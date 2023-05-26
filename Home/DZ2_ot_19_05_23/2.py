# Задание 2
# Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
# на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
maxnum = num1
if maxnum < num2:
    maxnum = num2
else:
    maxnum = maxnum
if maxnum < num3:
    maxnum = num3
else:
    maxnum = maxnum
minnum = num1
if minnum > num2:
    minnum = num2
else:
    minnum = minnum
if minnum > num3:
    minnum = num3
else:
    minnum = minnum
srednum = (num1 + num2 + num3)/2
vybor = input("Выберите желаемую операцию:\n1 - Вывести наибольшее число из трёх\n2 - Вывести наименьшее число их трёх\n3 - Вывести среднеарифметическое трёх чисел\n")
if vybor == "1":
    print(f"Наибольшее из введённых чисел: {maxnum}")
elif vybor == "2":
    print(f"Наименьшее из введённых чисел: {minnum}")
elif vybor == "3":
    print(f"Среднеарифметическое трёх чисел: {srednum}")
else:
    print("Ошибка. Необходимо было выбрать либо 1, либо 2, либо 3. Перезапустите программу.")