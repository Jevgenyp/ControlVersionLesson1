txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "а" or "б" or "в"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')