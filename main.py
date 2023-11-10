# Запрашиваем последовательность чисел
numb_list = [int(x) for x in input("Введите через пробел список положительных, целых чисел: ").split()]
number = int(input("Введите любое число в диапазоне списка: ")) #Запрашиваем число

def check_numb_list(): # Провека соответсвия. Не понял для чего, т.к. изначально заданы условия для ввода только чисел
    for i in numb_list: # и при вводе букв просто выдает ошибку. А через строку показалось слишком много операций.
        if isinstance(i, int) and i >= 0:
            return True
        else:
            return f"Введено не правильное значение списка"
    for i in number:
        if isinstance(i, int) and i >= 0:
            return True
        else:
            return f"Введено не правильное числовое значение"

def merge_sort(numb_list):
    if len(numb_list) < 2:
        return numb_list[:]
    else:
        middle = len(numb_list) // 2
        left = merge_sort(numb_list[:middle])
        right = merge_sort(numb_list[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

array = merge_sort(numb_list) # Помещаем отсортированный массив в переменную
def element_position(array, number, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if array[middle - 1] < number and number <=array[middle]:
        return [middle - 1]
    elif number < array[middle]:
        return element_position(array, number, left, middle - 1)
    elif number == array[middle - 1]:
        return element_position(array, number, left, middle - 1)
    else:
        return element_position(array, number, middle + 1, right)

#Задаем критерии для обозначения границ списка
left = array[0] #Левая граница
right = array[-1] #Правая граница

print(array)
if number < left or number > right:
    print("Введите значение в пределах указанного списка")
else:
    print(element_position(array, number, 0, len(array) - 1))