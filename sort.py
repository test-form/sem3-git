list_a = [4, 9, 0, 17, 23, 4, 1, 0]
n = len(list_a)
# Сортировка пузырьком


def bubble_sort(a, n):

    for i in range(n):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(bubble_sort(list_a, n))

# Сортировка перемешиванием


def cocktail_shaker_sort(a, n):
    left, right = 0, n - 1
    while left <= right:
        swapped = False

        for i in range(left, right):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        right -= 1

        for i in range(right, left, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swapped = True
        left += 1

        if not swapped:
            break
    return a


print(cocktail_shaker_sort(list_a, n))

# Сортировка вставками


def insertion_sort(a, n):
    for i in range(n):
        tmp = a[i]
        j = i - 1
        while tmp < a[j] and j>= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = tmp
    return a

print(insertion_sort(list_a, n))


# Сортировка выбором

def selection_sort(a, n):
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if a[j] < a[max_index]:
                max_index = j
        a[i], a[max_index] = a[max_index], a[i]
    return a

print(selection_sort(list_a, n))