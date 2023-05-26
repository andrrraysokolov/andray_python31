# myName = "andray"
# # start = int(input("Введите начальное значение"))
# # end = int(input("Введите конечное значение"))
# # for i in range (start,end + 1):   # (начало цикла, конец цикла, шаг)
# #     print (i)

# myName = "andray"
# for i in range (0,2 +1):
#     print(i)
# for i in myName:
#     print(i)

# myName = "andray"
# for i in myName:
#     print(i)
#     if i == "d":
#         break

# myName = "andray"
# for i in range (0, 29):
#     if i % 2 != 0:
#         print(i)

# a = 2
# b = 3
# if a + b == 5:
#     for i in range (0,10):
#         print((a+b)*i)

# x = int(input("Введите число на проверку простого числа"))
# for i in range (2,x+1):
#     if x % i == 0 and x != i:
#         print("Число сложное")
#         break
#     elif i == x:
#         print("Число простое")

# вывести чётные числа, кратные 6
# Пользователь запрашивает, какую таблицу умножения вывести для него, и программа выводит.

# endcount = int(input("Выводим чётные числа, кратные семи. Назначьте точку окончания вывода:\n"))
# for i in range (0, endcount + 1):
#     if i % 7 == 0 and i % 2 == 0:
#         print(i)


# choicenum = int(input("Для какого числа вывести таблицу умножения:\n"))
# print (f"Таблица умножения для числа {choicenum}:")
# for i in range (1, 10):
#     print (f"{i} x {choicenum} = {choicenum*i}")

# sum = 0
# for i in range (0, 10):
#     sum = sum + i
#     print (sum)

# i = 0
# b = 10
# while i < 10 and b > 0:
#     print(i)
#     print(b)
#     i = i + 1
#     b = b - 3

# i = 0
# b = 10
# while i != 11 and i < 100:
#     print(i)
#     i = i + 23

# i = 0
# b = 10
# while True:
#     print (12)
#     i = i + 1
#     if i > 10:
#         break

# print("Второй цикл")
# x = True
# while x == True:
#     print (i)
#     i = i + 1
#     if i > 15:
#         x = False



# myName = "andray"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i+=1 # i = i + 1

#посчитать факториал введенного пользователем числа

chislo = int(input("Введите число для расчёта факториала:\n"))
faktor = 1
i = 1
while i <= chislo:
    faktor = faktor * i
    i = i + 1
print (faktor)










