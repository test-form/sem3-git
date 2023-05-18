# Урок N5. Логические и условные операторы
#
# Задание N1. Пользователь вводит целое число. Выведите его строку-описание вида
# "отрицательное четное число", "нулевое число", "положительное нечетное число",
# например, численным описанием числа 190 является строка "положительное четное число".
# Если число не является четным - выведите сообщение "число не является четным"

def numbers(num):
	if num > 0 and num % 2 == 0:
		return f"Положительное чётное число"
	if num < 0 and num % 2 == 0:
		return f"Отрицательное чётное число"
	if num == 0:
		return f"Нулевое число"
	if num % 2 != 0:
		return f"Число не является чётным"

print(numbers(7))

# Задание N2. Дано слово из маленьких латинских букв. Сколько там согласных и
# гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».Для решения задачи
# создайте переменную и в неё положите слово с помощью input() А также определите
# количество каждой из этих гласных букв Если какой-то из перечисленных букв нет
# -Выведите False

vowels = ['a', 'e', 'i', 'o', 'u']
def vowel(word):
	count = 0
	for letter in word:
		if letter in vowels:
			count += 1
	if count == 0:
		return False
	else:
		return count

print(vowel('hello'))

# Задание N3. Два инвестора -Майкл и Иван хотят вложиться в стартап.
# Фаундеры сказали, что минимальная сумма инвестиций -X долларов, больше инвестировать
# можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться
# - выведите 2, если только Майкл - Mike, если только Иван -Ivan, если не могут
# по отдельности, но вместе им хватает -1, если никто -0.

def investments(A,B,X):
	if A >= X and B >= X:
		return 2
	if A >= X and B < X:
		return f'Mike'
	if B >= X and A < X:
		return f'Ivan'
	if A < X and B < X and A + B >= X:
		return -1
	if A < X and B < X and A + B < X:
		return 0

print(investments(13,13,10))
print(investments(13,5,10))
print(investments(5,13,10))
print(investments(5,5,10))
print(investments(1,1,10))