""""Алгоритм сортировки выбором"""


def selection_sort(list_for_sort: list):
    """
    Функция производит сортировку массива методом выбора. Сложность алгоритма 0(n**2).
    :param list_for_sort: list - список передаваемый для сортировки
    :return result: list - отсортированный список
    """
    work_list = list_for_sort
    for i in range(len(work_list)):
        index_min = i
        for j in range(i+1, len(work_list)):
            if work_list[j] < work_list[index_min]:
                index_min = j
        tmp = work_list[index_min]
        work_list[index_min] = work_list[i]
        work_list[i] = tmp
    return work_list
