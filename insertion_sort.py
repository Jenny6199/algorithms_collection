""" Алгоритм сортировки вставками."""


def insertion_sort(list_for_sort: list):
    a = list_for_sort
    for i in range(len(a)):
        v = a[i]
        j = i
        while (a[j-1] > v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
        print(a)
    return a
