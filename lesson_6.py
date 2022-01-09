import numpy as np

# Решить задачу про таблицу сотрудников используя numpy (вывести на экран информацию о сотрудниках,
# принятых на работу после 2012 года и с ЗП выше 2000; напечатать можно без форматирования)

workers_table = np.array([
    [1, 'B', 1000, 2013],
    [2, 'B', 1500, 2014],
    [3, 'B', 1800, 2012],
    [4, 'A', 2500, 2016],
    [5, 'A', 3500, 2017],
    [6, 'A', 4500, 2011],
], dtype=object)

table_work = workers_table[
    (workers_table[:, 2] > 2000) &
    (workers_table[:, 3] > 2012)]
print(table_work)

# В таблице сотрудников из предыдущей задачи, добавить еще один столбец, где записать разницу между ЗП сотрудника
# и средней ЗП всех сотрудников

mean_sum_salary = np.int_(np.sum(workers_table[:, 2]) / len(workers_table))

new_workers_table = np.insert(workers_table, 4, values=workers_table[:, 2] - mean_sum_salary, axis=1)
print(new_workers_table)


# В таблице сотрудников найти и вывести на экран минимальный год приема на работу в каждом департаменте
min_work_tab_a = workers_table[np.where((workers_table[:, 1] == 'A'))]
min_work_tab_b = workers_table[np.where((workers_table[:, 1] == 'B'))]

print(f'minimum year of recruiting department A: {np.min(min_work_tab_a[:, 3])}\n'
      f'minimum year of recruiting department B: {np.min(min_work_tab_b[:, 3])}')

departments = np.unique(workers_table[:, 1])
for depart in departments:
    dep_works = workers_table[workers_table[:, 1] == depart]

print(departments, dep_works)
# Дана таблица A
# Задача - нормализовать колонки (сделать так, чтобы длина векторов в колонках была 1)

A = np.array([
    [2, 5, 8, 56],
    [4, 9, 1, 23],
    [6, 12, 84, 55]
])

len_x = np.sqrt(np.sum(A[:, 0] ** 2))
len_y = np.sqrt(np.sum(A[:, 1] ** 2))
len_z = np.sqrt(np.sum(A[:, 2] ** 2))
len_q = np.sqrt(np.sum(A[:, 3] ** 2))
print(len_x, len_y, len_z, len_q)

hatch_x = np.sum((A[:, 0] / len_x) ** 2)
hatch_y = np.sum((A[:, 1] / len_y) ** 2)
hatch_z = np.sum((A[:, 2] / len_z) ** 2)
hatch_q = np.sum((A[:, 3] / len_q) ** 2)
print(hatch_x, hatch_y, hatch_z, hatch_q)

