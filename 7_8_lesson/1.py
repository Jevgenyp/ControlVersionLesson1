# b = 5
# c = 0
# try:
#     a = b / c
# except ZeroDivisionError: 
#     print('На ноль делить нельзя')
#     a = 0
# print(a)
    
file = open('C:/Users/Jev/Desktop/GeekBrains/Python/HomeworkPy/Homework_Phyton/7_8_lesson/1.txt', 'r', encoding='utf-8')
text = file.read()
print(text)
file.close()
