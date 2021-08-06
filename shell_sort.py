""" Алгоритм сортировки списка методом Шелла."""


def shell_sort(a):
    """
    Функция сортирует список по методу Шелла
    :param a:list - сортируемый список.
    :return a:list - отсортированный список.
    """
    def new_increment(_a: list):
        """Вспомогательная функция"""
        k = int(len(_a) / 2)
        yield k
        while k != 1:
            if k == 2:
                k = 1
            else:
                k = int(round(k / 2.2))
            yield k

    for increment in new_increment(a):
        for i in range(increment, len(a)):
            for j in range(i, increment - 1, -increment):
                if a[j - increment] < a[j]:
                    break
                a[j], a[j - increment] = a[j - increment], a[j]
    return a
