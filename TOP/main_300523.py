#таблица умножения для 10 чисел - цикл в цикле

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,j)

##таймер с помощью for
# import time
# for h in range(0,24):
#     for m in range(0,60):
#         for s in range(0,60):
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1)

##таймер с помощью while
# import time
# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(h, m, s)
#             time.sleep(1/10)
#             s = s + 1
#         m = m + 1
#     h = h + 1

print("Регистрация персонажа")
reg = 0
while reg < 1:
    reg_gender = 0
    while reg_gender < 1:
        gender = input("Выберите пол персонажа:\n1 - мужской\n2 - женский\n")
        if gender == "1":
            gender = "Мужской"
            reg_gender = reg_gender + 1
        elif gender == "2":
            gender = "Женский"
            reg_gender+=1
        else:
            print("Выберите из перечисленного - 1 или 2")
        if reg_gender == 1:
            print(f"ОК, ваш пол - {gender}.")
            reg_race = 0
            while reg_race < 1:
                race = input("Выберите расу персонажа:\n1 - человек\n2 - эльф\n0 - вернуться на предыдущий этап\n")
                if race == "1":
                    race = "Человек"
                    reg_race = reg_race + 1
                elif race == "2":
                    race = "Эльф"
                    reg_race+=1
                elif race == "0":
                    reg_gender = 0
                    break
                else:
                    print("Выберите из перечисленного - 1 или 2")
                if reg_race == 1:
                    print(f"ОК, ваш пол - {gender}, ваша раса - {race}.")
                    reg_class = 0
                    while reg_class < 1:
                        class1 = input("Выберите класс персонажа:\n1 - лучник\n2 - безработный\n0 - вернуться на предыдущий этап\nstart - вернуться в начало\n")
                        if class1 == "1":
                            class1 = "Лучник"
                            reg_class= reg_class + 1
                        elif class1 == "2":
                            class1 = "безработный"
                            reg_class+=1
                        elif class1 == "0":
                            reg_race = 0
                            break
                        elif class1 == "start":
                            reg_gender = 0
                            break
                        else:
                            print("Выберите из перечисленного - 1 или 2")
                
    print(f"Вы зарегистрированы, ваш пол - {gender}, ваша раса - {race}, ваш класс - {class1}")
    reg+=1