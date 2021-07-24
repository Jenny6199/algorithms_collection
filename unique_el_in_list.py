"""Алгоритм поиска уникальных значений в списке"""

form random import randrange, seed
seed(1)


def get_unique_el_for_list(array: list):
	"""
	Функция осуществляет поиск уникальных значений в списке.
	:param - array: list - принимает список в котором будет произведен поиск.
	:return - no_repeat: list-  возвращает список уникальных элементов заданного списка. 
	"""
	no_repeat = list()
	for i in range(n):
		flag = True
		for j in range(n):
			if a[i] == a[j] and i != j:
				flag = False
				break
		if flag:
		no_repeat.append(a[i])
	return no_repeat


array_1 = [randrange(0, 100) for _ in range(20)]
print(get_unique_el_for_list(array_1))
