# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# real_num = input("Введите вещественное число:   ")
# sum = 0

# for i in real_num:

#     if i == "e":   # игнорирование "е" и следующие за ней знаки,если цифр после запятой будет много 
#         break
#     if i in ("0123456789"):
#         sum += int(i)
# print("сумма цифр вещественного числа равна ",sum)
#-------------------------------------------

real_num = input("Введите вещественное число:   ")

def func(x):   
    if x == "." :return 0
    return int(x)
li = list(map(func,real_num))                              # функция map
print("сумма цифр вещественного числа равна ",sum(li))       
