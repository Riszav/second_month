# 1. Написать функцию bubble_sort или selection_sort, принимающую в качестве входящего параметра не отсортированный
#    список.
# 2. Алгоритм функции должен сортировать список методом пузырьковой сортировки или методом сортировки выбором.
# 3. Функция в итоге должна возвращать отсортированный список. Применить 1 раз данную функцию
# 4. Написать функцию binary_search, принимающую в качестве входящего параметра элемент для поиска и список в котором
#    необходимо искать.
# 5. Алгоритм должен искать с помощью двоичного поиска, изображенного на блок-схеме презентации.
# 6. Функция в итоге должна распечатать результат. Применить 1 раз эту функцию
def bubble_sort(list):
    sorted_list=False

    while not sorted_list:
        swap_value=False
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                value = list[i]
                del list[i]
                list.insert(i+1,value)
                swap_value=True
            else:
                continue
        if not swap_value:
            return list

list_1 = [1,8,5,3,4,6,7,2,5,19,5,8,20]
bubble_sort(list_1)
print(f'----------------Отсортированный список----------------\n{list_1}')

def binary_search(list, value):
    n = len(list)
    result_ok = False
    first = 0
    last = n - 1
    while True:
        if first<=last and not result_ok:
            middle = (first+last) // 2
            # print(f'First {list[first]} Middle {list[middle]} Last {list[last]}')
            if value == list[middle]:
                first = middle
                last = first
                result_ok = True
                pos = middle
            elif value > list[middle]:
                first = middle + 1
            else:
                last = middle - 1
        else:
            if result_ok == True:
                print(f'Элемент {value} найден\nИндекс элемента: {pos}')
                break
            else:
                print(f'Элемент {value} не найден')
                break

list_2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,27,28,30]
print(f'------------------Список для поиска:------------------\n{list_2}')
value=int(input('Введите число для поиска: '))
binary_search(list_2,value)