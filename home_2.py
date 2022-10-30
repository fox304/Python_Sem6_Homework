# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#----------------------------------------------------
# from decimal import Decimal

# given_list_real = [1.5, 1.2, 3.003, 5, 10.01]

# def convert():

    # list_decimal = list(map(Decimal, list_str))
    # list_fractal = [i - int(i) for i in list_decimal]
    # list_without_zero = list(filter(lambda x: x != 0, list_fractal))
    # return (list_without_zero)

# res = convert()
# result = max(res) - min(res)
# print(result)
    

 # -------------------------------------------------------------------------    
from math import trunc

given_list_real = [1.5, 1.2, 3.003, 5, 10.01]
def convert():

    a1 = [round(i - trunc(i),8) for i in given_list_real]    # ушёл от Decimal
    a3 = list(filter(None, a1))                       # использовал   None в  filter          
    return max(a3) - min(a3)

print(convert())
    
# -------------------------------------------------------------------------  


