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

print("Заполните информацию")
myName = input("Введите имя: ")
myAge = int(input("Введите возраст: "))
myCountry = input("Ваше гражданство: ")
print("")
print("Информация о пользователе:")
print("Имя", myName)
print("Ваш возраст, умноженный на 2:", myAge*2)
print("Ваше гражданство:", myCountry)
