##Запросить у пользователя трехзначное и число и проверить,
##есть ли в нем одинаковые цифры.

chislo = int(input("Проверим, есть ли в вашем числе одинаковые цифры.\nВведите любое трёхзначное число:\n"))
cifr1 = int(chislo // 100)
cifr2 = int((chislo // 10) % 10)
cifr3 = int(chislo % 10)
if chislo >= 100 and chislo <= 999:
    if cifr1 == cifr2 or cifr1 == cifr3 or cifr2 == cifr3:
        print ("В вашем числе есть одинаковые цифры.")
    else:
        print ("Введённое вами число состоит из трёх разных цифр.")
else:
    print ("Введённое вами число - не трёхзначное. Перезапустите программу и введите трёхзначное число.")



