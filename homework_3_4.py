


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