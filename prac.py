
array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

num = int(input('Введите число: '))

def error():
    if " " not in array:
        print('Нет пробелов')
        array = input('Введите числа через пробел: ')
    else:
        array = array.split()

print(type(array))
array = [int(item) for item in array]
def sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
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

array = sort(array)
print(array)



def binary_search(array, num, left, right):
        if left > right:
            return False

        middle = (right + left) // 2
        if array[middle] == num:
            return middle
        elif num < array[middle]:
            return binary_search(array, num, left, middle - 1)
        else:
            return binary_search(array, num, middle + 1, right)



max_num = max(array)
print('Максимальный элемент', max_num)
print(f'Индекс введенного элемента: {binary_search(array, num, 0, len(array))}')
if not binary_search(array, num, 0, len(array)):
    i = min(array, key=lambda x: (abs(x - num), x))
    ind = array.index(i)
    max_ind = ind + 1
    min_ind = ind - 1
    if i < num:
        print(f''''Введен элемент которого нет в списке' 
Ближайший меньший элемент: {i}, его индекс: {ind}
Ближайший больший элемент: {array[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''Введен элемент которого нет в списке
Ближайший больший элемент: {i}, его индекс: {array.index(i)}
В списке нет меньшего элемента''')
    elif i > num:
        print(f'''Введен элемент которого нет в списке
Ближайший больший элемент: {i}, его индекс: {array.index(i)}
Ближайший меньший элемент: {array[min_ind]} его индекс: {min_ind}''')
    elif array.index(i) == 0:
        print(f'Индекс введенного элемента: {array.index(i)}')
else:
    print(f'Индекс введенного элемента: {binary_search(array, num, 0, len(array))}')











