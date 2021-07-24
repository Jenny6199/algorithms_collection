""" Алгоритм слияния двух отсортированных списков."""


def sum_sort_array(mass_a: list, mass_b: list):
    """
    :param mass_a: list, sorted
    :param mass_b: list, sorted
    :return: sorted mass_c = sort(mass_a + mass_b)
    """

    c = [0] * int(len(mass_a) + len(mass_b))
    v, k, n = 0, 0, 0
    while v < len(mass_a) and k < len(mass_b):
        if mass_a[v] <= mass_b[k]:
            c[n] = mass_a[v]
            v += 1
            n += 1
        else:
            c[n] = mass_b[k]
            k += 1
            n += 1
    while v < len(mass_a):
        c[n] = mass_a[v]
        v += 1
        n += 1
    while k < len(mass_b):
        c[n] = mass_b[k]
        k += 1
        n += 1
    return c
