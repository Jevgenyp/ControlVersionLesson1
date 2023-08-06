# b = 5
# c = 0
# try:
#     a = b / c
# except ZeroDivisionError: 
#     print('На ноль делить нельзя')
#     a = 0
# print(a)
    
with open('C:/Users/Jev/Desktop/GeekBrains/Python/HomeworkPy/Homework_Phyton/7_8_lesson/1.txt', 'r', encoding='utf-8') as file:
    for stroki in file:
        print(stroki.strip())
print()


