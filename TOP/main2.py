num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
otvet1 = input("Какую из 3-х операций вы хотите совершить с указанными числами?\n1. Посчитать сумму двух чисел\n2. Посчитать разницу\n3. Посчитать среднеарифметическое\n4. Посчитать произведение\n")
if otvet1 == "1":
    print(f"Сумма чисел равна {num1+num2}")
elif otvet1 == "2":
    print(f"Разница чисел равна {num1-num2}")
elif otvet1 == "3":
    print(f"Среднеарифметическое равно {(num1+num2)/2}")
elif otvet1 == "4":
    print(f"Произведение чисел равно {num1*num2}")
else:
    print("Вы не сделали свой выбор. Нужно было выбрать пункт от 1 до 4.")


    




