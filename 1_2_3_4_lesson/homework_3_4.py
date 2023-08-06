


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# 1.  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list_a = [2, 3, 5, 9, 3]
# numbers_sum = 0
# i = 1
# for i in range(1, len(list_a), 2):
#     numbers_sum += list_a[i]
# print(numbers_sum)    

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import sample

# def fill_list(number):
#     ls=sample(range(1,number*2),number)
#     return ls

# def multy(lst):
#     lst1=[]
#     len_lst=len(lst)//2
#     for i in range(len_lst):
#         lst1.append(lst[i]*lst[len(lst)-1-i])
    
#     if len(lst) % 2 == 1:
#         lst1.append(lst[len(lst) // 2 ] ** 2)
         
        
#     return lst1

# start_list=fill_list(int(input('Enter a number ')))
# print (start_list)
# print (multy(start_list))
    
# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))

#  4. Напишите программу, которая будет преобразовывать десятичное число в двоичное

# s = ""
# n = int(input("Введите число: "))
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(s)

# Вычислить число pi c заданной точностью d.

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')



# k = 1
# x = 0
# for k in range(1, 1000000):
#     x = x+4*((-1)**(k+1))/(2*k-1)
# print(round(x, d))

#2. Задайте натуральное число N. Напишите программу, которая составит
#  список простых множителей числа N.

# n = int(input('n: '))
# list = [] 
# i = 2
# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n /= i
#     else:
#         i += 1
# print(list)

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# dct = {}
# new_lst = []
# for i in lst:
#     a = lst.count(i)
#     dct.update({i: a})

# a = 0
# keys = list(dct.keys())
# for i in dct:
#     if dct[i] == 1:
#         new_lst.append(keys[a])
#         a += 1
#     else:
#         a += 1

# print(f"Список из неповторяющихся элементов: {new_lst}")

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

print('Введите степень k! ')
k = int(input("Введите степень k: "))

factor = []
for i in range(1, k +2):
    factor.append(randint(1, 101))

result = []
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}')
    signs = randint(0, 1)
    if signs == 1:
        result.append('+')
    elif signs == 0:
        result.append('-')
    k -= 1

result.pop(-1)
result.append('=0')

record = open('data.txt', 'w')
record.write(''.join(result))
record.close()

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')
