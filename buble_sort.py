""" Алгоритм сортировки 'пузырьком'."""

sorted_list = [5, 2, 7, 4, 0, 9, 8, 6]


def bubble_sort(sorted_arr: list):
    """
    Сортировка списка методом 'пузырька'. Сложность O(n**2).1
    :param sorted_arr: list - сортируемый список
    :return: result: list - отсортированный список
    """
    n = 1
    while n < len(sorted_arr):
        for i in range(len(sorted_arr) - n):
            if sorted_arr[i] > sorted_arr[i + 1]:
                sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
        n += 1
    return sorted_arr
