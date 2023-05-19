#! /usr/bin/env python
# -*- coding: utf-8 -*-


#type_int = 1 # целые числа (int)
#type_float = 1.23 # числа с плавающей точкой
#type_str = "Строки пишутся в кавычках"
#type_bool_one = True # булевы значения истина (правда)
#type_bool_two = False # булевы значения ложь
#type_none = None

# a = 123
# print(a * 2,type(a)) #int
# a = str(a)
# print (a * 2,type(a)) #str
# a = float(a) #float
# print(a * 2,type(a))

# b = "Привет"
# print(b,type(b))
# b = int(b)
# print (b,type(b))

# z = float(input("Введите число - мы умножим его на 2: "))
# print (z * 2)

# print("Заполните информацию")
# myName = input("Введите имя: ")
# myAge = int(input("Введите возраст: "))
# myCountry = input("Ваше гражданство: ")
# print("")
# print("Информация о пользователе:")
# print("Имя", myName)
# print("Ваш возраст, умноженный на 2:", myAge*2)
# print("Ваше гражданство:", myCountry)

# myName = "and"
# print ("привет" + " " + myName)
# print (f"привет {2*3}")
# print ("привет", " ", "мир!")

# z = int(input("Введите число: "))
# print (z//10)
# print (z%10)

# z = int(input("Введите число: "))
# a = z//100
# b = (z//10)%10
# c = z%10
# d = a+b+c
# print(a)
# print(b)
# print(c)
# print(d)

# a = str(input("Введите первую цифру: "))
# b = str(input("Введите вторую цифру: "))
# c = a+b
# c = int(c)
# print(c)

# a = 5
# b = 10
# if a < b or b > 10:
#     print("if выполнился")
# else:
#     print("else выполнился")

# a = 5
# b = 10
# if (a < b and b > 10) or a == 5:
#     print("if выполнился")
# else:
#     print("else выполнился")

# a = 10
# b = 10
# if a < b:
#     print("if выполнился")
# elif a > b:
#     print("elif выполнился")
# else:
#     print("else выполнился")

# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# if login == "admin":
#     if password == "admin":
#         print ("Вход выполнен")
#     else:
#         print("Неверный логин и пароль на втором этапе")
# else:
#     print("Неверный логин и пароль на первом этапе")

q1 = input("У вас пока 0 баллов. Зимой летом одним цветом? ")
score = 0
if q1 == "ёлка" or q1 == "елка":
    score = score + 1
    print(f"Ответ верный. У вас {score} баллов.")   
else:
    score = score - 1
    print(f"Ответ неверный. У вас {score} баллов")
q2 = input("Какого цвета солнце? ")
if q2 == "жёлтое" or q2 == "желтое":
    score = score + 1
    print(f"Ответ верный. У вас {score} баллов.")
else:
    score = score - 1
    print(f"Ответ неверный. У вас {score} баллов")
q3 = input("Что говорит собака? ")
if q3 == "гав":
    score = score + 1
    print(f"Ответ верный. У вас {score} баллов.")
else:
    score = score - 1
    print(f"Ответ неверный. У вас {score} баллов")
q4 = input("Что говорит кошка? ")
if q4 == "мяу":
    score = score + 1
    print(f"Ответ верный. У вас {score} баллов.")
else:
    score = score - 1
    print(f"Ответ неверный. У вас {score} баллов")
q5 = input("Что говорит корова? ")
if q5 == "му":
    score = score + 1
    print(f"Ответ верный. У вас {score} баллов.")
else:
    score = score - 1
    print(f"Ответ неверный. У вас {score} баллов")
if score >= 3:
    ask = input(f"Вы набрали как минимум 3 балла и достойны доп вопроса. Хотите ещё один вопрос? ")
    if input == "yes":
        q6 = input("Столица России? ")
        if q6 == "Москва" or q6 == "москва":
            score = score + 1
            print(f"Ответ верный. Ты победил в суперигре с {score} баллов.")
        else:
            score = score - 1
            print(f"Ответ неверный. Ты всё равно молодец с {score} баллов.")
    else:
        print("Не хотите как хотите.")
else:
    print("Ты проиграл, набрав меньше 3 очков. Доп вопроса не будет.")



