import os

def load_data(file_name):
    """
    Загружает данные из файла в словарь.
    """
    data = {}
    if os.path.isfile(file_name):
        with open(file_name, 'r') as f:
            for line in f:
                name, surname, patronymic, phone_number = line.strip().split(',')
                data[name] = [surname, patronymic, phone_number]
    return data

def save_data(file_name, data):
    """
    Сохраняет данные из словаря в файл.
    """
    with open(file_name, 'w') as f:
        for name, info in data.items():
            surname, patronymic, phone_number = info
            f.write(f"{name},{surname},{patronymic},{phone_number}\n")

def print_data(data):
    """
    Выводит все записи в телефонной книге.
    """
    print("\nТелефонная книга:")
    for name, info in data.items():
        surname, patronymic, phone_number = info
        print(f"{name} {surname} {patronymic} {phone_number}")

def search_data(data, parameter): # Ищет даже если вводить маленькие буквы(Подсмотрел это решение)
    result = []
    for name in data:
        if parameter.lower() in name.lower() or parameter.lower() in data[name][0].lower() or parameter.lower() in data[name][1].lower() or parameter.lower() in data[name][2].lower():
            result.append(f"{name}: {data[name][0]}, {data[name][1]}, {data[name][2]}")
    return result

def edit(file_name, data):
    print("Редактирование записи")
    search_key = input("Введите имя или фамилию для поиска: ").strip().lower()

    # Находим индекс записи для редактирования
    found_index = None
    for name, info in data.items():
        if search_key in name.lower():
            found_index = name
            print(f"Вы хотели {name} ")
            answer = input("да или нет?")
            if answer == "да":
            
                break
    else: 
        edit()
            

    # Если запись не найдена
    if found_index is None:
        print("Запись не найдена.")
        return data

    # Редактируем запись
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    data[found_index] = [surname, patronymic, phone_number]
    save_data(file_name, data)

    print("Запись успешно изменена.")
    return data

def delete_data(data, name):
    """
    Удаляет запись из словаря по имени.
    """
    if name in data:
        del data[name]
        print("Запись успешно удалена.")
    else:
        print("Запись не найдена.")


def main():
    file_name = 'data.txt'
    data = load_data(file_name)

    while True:
        print("\nМеню:")
        print("1. Показать все записи")
        print("2. Добавить запись")
        print("3. Поиск записи")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print_data(data)
        elif choice == '2':
            name = input("Введите имя: ")
            surname = input("Введите фамилию: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            data[name] = [surname, patronymic, phone_number]
            save_data(file_name, data)
            print("Запись добавлена.")
        elif choice == '3':
            parameter = input("Введите параметр для поиска: ")
            result = search_data(data, parameter)
            if result:
                print("\nРезультаты поиска:")
                for r in result:
                    print(r)
            else:
                print("Запись не найдена.")
        elif choice == '4':
            edit(file_name,data)
        
        elif choice == '5':
            name = input("Введите имя для удаления: ")
            delete_data(data, name)
            save_data(file_name, data)
            
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
