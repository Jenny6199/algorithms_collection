""" Алгоритм быстрой сортировки 'на месте'."""
import random


def qsort_inplace(sorted_list, start=0, end=None):
    """
    Функция производит сортировку списка методом быстрой сортировки 'на месте'
    """
    def subpart(sorted_list: list, start: int, end: int, pivot_index: int):
        """
        Вспомогательная функция
        :param sorted_list: сортируемый список
        :param start: int стартовый индекс
        :param end: int конечный индекс
        :param pivot_index: int барьерный индекс
        """
        sorted_list[start], sorted_list[pivot_index] = sorted_list[pivot_index], sorted_list[start]
        pivot = sorted_list[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if sorted_list[y] <= pivot:
                sorted_list[y], sorted_list[x] = sorted_list[x], sorted_list[y]
                x += 1
            y += 1

        sorted_list[start], sorted_list[x - 1] = sorted_list[x - 1], sorted_list[start]
        return x - 1

    if end is None:
        end = len(sorted_list) - 1
    if end - start < 1:
        return

    pivot_index = random.randint(start, end)
    x = subpart(sorted_list, start, end, pivot_index)
    qsort_inplace(sorted_list, start, x - 1)
    qsort_inplace(sorted_list, x + 1, end)


ary = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]
print(ary)
qsort_inplace(ary)
print(ary)
