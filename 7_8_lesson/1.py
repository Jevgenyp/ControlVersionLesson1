b = 5
c = 0
try:
    a = b / c
except ZeroDivisionError: 
    print('На ноль делить нельзя')
    a = 0
print(a)
    