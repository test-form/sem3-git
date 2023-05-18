# Урок N11. Функции
#
# Задание N1. Создайте функцию, которая принимает в качестве параметра -натуральное
# целое число.Данная функция находит факториал полученного числа Например, факториал числа 3
# это число 6.Теперь создайте список факториалов чисел от получившегося ранее факториала 6,
# до 1. В итоге, на вход программа получает например число 3, возвращает число 6(факториал числа 3)
# и вам нужно сделать список из факториалов числа 6в убывающем порядке. Находим факториал числа 6
# -это 720, затем от числа 5-это 120и так далее вплоть до 1 То есть, результирующий список
# будет выглядеть в нашем примере так: [720, 120, 24, 6, 2, 1]

def fact(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n > 2:
		return fact(n - 1) * n

n = int(input("Введите число, факториал которого надо найти: "))
print(fact(n))
list_a = []
for i in range(n,0,-1):
	list_a.append(fact(i))
print(list_a)

# Задание №2
# В Урок №10. Задание №1 вы создавали словарь с информацией о питомце. Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
# Подробный требуемый функционал будет ниже. Пока что справка:
# ● Создайте функцию create
# ● Создайте функцию read
# ● Создайте функцию update
# ● Создайте функцию delete
# ● Используйте словарь pets, который будет предоставлен ниже, либо создайте свой аналогичный
# Функция create:
# Данная функция будет создавать новую запись с информацией о питомце и добавлять эту информацию в наш словарь pets
# Функция read
# Данная функция будет отображать информацию о запрашиваемом питомце в виде:
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
# Функция update
# Данная функция будет обновлять информацию об указанном питомце
# Функция delete
# Данная функция будет удалять запись о существующем питомце

import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def create():
    last_key = collections.deque(pets, maxlen=1)[0]
    new_key = last_key + 1
    name = input("Введите имя нового питомца: ")
    animal_type = input("Введите вид нового питомца: ")
    owner = input("Введите имя владельца нового питомца: ")
    flag = True
    while flag:
        try:
            age = int(input("Введите возраст нового питомца: "))
            if age <= 0:
                print("Возраст должен быть больше 0.")
                continue
            flag = False
        except ValueError:
            print("Некорректный ввод. Введите число.")
    new_pet = {
        "Вид питомца": animal_type,
        "Возраст питомца": age,
        "Имя владельца": owner,
    }
    pets[new_key] = {name: new_pet}
    print(f"Добавлен новый питомец с ID {new_key} и именем {name}.")


def read():
    id = int(input("Введите ID питомца: "))
    if id in pets:
        pet_info = pets[id]
        print(f"Это {pet_info[list(pet_info.keys())[0]]['Вид питомца']} по кличке \"{list(pet_info.keys())[0]}\". Возраст питомца: {pet_info[list(pet_info.keys())[0]]['Возраст питомца']} {get_suffix(pet_info[list(pet_info.keys())[0]]['Возраст питомца'])}. Имя владельца: {pet_info[list(pet_info.keys())[0]]['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден")

def pets_list():
    for id, pet in pets.items():
        pet_name = list(pet.keys())[0]
        pet_info = pet[pet_name]
        print(f"ID питомца: {id}, Имя питомца: {pet_name}, Вид питомца: {pet_info['Вид питомца']}, Возраст питомца: {pet_info['Возраст питомца']} {get_suffix(pet_info['Возраст питомца'])}, Имя владельца: {pet_info['Имя владельца']}")

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    if ID in pets:
        return pets.get(ID)
    else:
        return None


def update(ID):
    if ID not in pets:
        print(f"Питомец с ID {ID} не найден.")
        return
    pet_info = pets[ID][list(pets[ID].keys())[0]]
    print(f"Текущая информация о питомце:\n{pet_info}")
    animal_type = input("Введите новый вид питомца: ")
    age = int(input("Введите новый возраст питомца: "))
    owner = input("Введите новое имя владельца: ")
    pet_info.update({"Вид питомца": animal_type, "Возраст питомца": age, "Имя владельца": owner})
    print(f"Информация о питомце с ID {ID} обновлена.")

def delete(ID):
    if ID in pets.keys():
        del pets[ID]
        print(f"Питомец с ID {ID} удален из базы данных")
    else:
        print(f"Питомец с ID {ID} не найден в базе данных")

command = '0'
while command != 'stop':
	command = input("Введите команду (create, delete, read, stop): ")
	if command == 'create':
		create()
	elif command == 'delete':
		ID = int(input("Введите ID питомца: "))
		delete(ID)
	elif command == 'read':
		read()
		pets_list()
	elif command == 'stop':
		command = 'stop'
	else:
		print("Неккоректная команда")