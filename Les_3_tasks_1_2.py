# Урок N3. Ввод-вывод и базовые переменные

# Задание N1. Давай представим, что мы пишем бэкенд для сайта ветеринарной клиники.
# Нам нужно написать программу, которая будет запрашивать у пользователя вид питомца,
# его возраст и кличку, а потом выведет все эти данные в одно предложение.
# Например:Это желторотый питон по кличке "Каа". Возраст: 34 года.


def pet():
	type_pet = input("Введите вид питомца: ")
	name_pet = input("Введите кличку питомца: ")
	age_pet = int(input("Введите возраст питомца: "))
	return f"Это {type_pet} по кличке {name_pet}. Возраст: {age_pet} года"

print(pet())

# Задание N2. А теперь мы с тобой напишем форму ввода ответа на тест по биологии
# для студентов. Он должен запрашивать по порядку этапы развития человека
# (проверим твое умение гуглить, что тоже очень важно для программиста.) и в конце
# вывести все стадии, разделенные знаком =>, что будет означать постепенный переход
# от одного к другому. В следующих уроках мы дополним эту форму до полноценного теста,
# который будет проверять правильность ответов, а пока -начнем с малого. Напоминаем,
# что разделить эти данные тебе поможет команда sep внутри команды print, например,
# чтобы разделить переменные знаком +нужно ввести: print(a1, a2, a3, sep='+')

def human_evolution_stages():
	dr = "дриопитек"
	rm = "рамапитек"
	au = "австралопитек"
	hu = "человек умелый"
	hp = "человек прямоходящий"
	pn = "неандерталец"
	na = "неоантроп"
	print(dr, rm, au, hu, hp, pn, na, sep='=>')

human_evolution_stages()