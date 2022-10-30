# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint

# n = int(input("Введите целое число "))

# with open("num.txt", "w") as pos:           # запись чисел в файл num.txt 
#     for i in range(n):
#         x = randint(-n, n)
#         pos.write(f"{x}\n")

# with open("num.txt", "r") as pos:
#     num_text = pos.read()

# num_text = num_text.split()
# product = 1
# for i in range(len(num_text)):
#     num_text[i] = int(num_text[i])          # превращение строк в целые  числа
#     product *= num_text[i]

# print(f"Произведение элементов данного списка {num_text} равно  {product} ")
#---------------------------------------------------------------------------

from random import randint

n = int(input("Введите целое число "))

with open("num.txt", "w") as pos:            
    for i in range(n):
        x = randint(-n, n)
        pos.write(f"{x}\n")

with open("num.txt", "r") as pos:
    num_text = pos.read()

num_text = num_text.split()
product = 1

for i in range(len(num_text)):           
    product = (lambda x,y:x*y)(product,int(num_text[i]))          # использование lambda

print(f"Произведение элементов данного списка {num_text} равно  {product} ")