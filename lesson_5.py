# Дано: 2 списка чисел
# Задача: создать список, элементы которого равны произведениям этих списков

list1 = [1, 2, 3]
list2 = [3, 4, 5]
res = list(map(lambda x, y: x * y, list1, list2))
print(res)

# Дано: таблица с информацией о сотрудниках. Каждый вложенный список содержит следующие элементы: номер сотрудника,
# департамент, ЗП и год приема на работу
# Задача: вывести на экран информацию о сотрудниках, принятых на работу после 2012 года и с ЗП выше 2000.
# Информация должна быть в следующем текстовом формате: "Number: 1, Dep: B, Salary: 1000, Year: 2019"

workers_table = [
    [1, 'B', 1000, 2013],
    [2, 'B', 1500, 2014],
    [3, 'B', 1800, 2012],
    [4, 'A', 2500, 2016],
    [5, 'A', 3500, 2017],
    [6, 'A', 4500, 2011],
]

elem = list(filter(lambda x: x[3] > 2012 and x[2] > 2000, workers_table))

for el in elem:
    print(f'Number: {el[0]}, Dep: {el[1]}, Salary: {el[2]}, Year: {el[3]}')


# Дано: два списка чисел
# Задача: добавить из второго списка в первый только те элементы, которых в нем еще нет

num_list = [1, 2, 3, 4, 5]
list_to_add = [1, 2, 3, 10, 100]

num_list.extend([item for item in list_to_add if item not in num_list])
print(list(num_list))

#num_list.extend(map(lambda s: s not in list_to_add, num_list))
#print(num_list)

list_of_stop_words = ["в", "и", "по", "за"]

# Строка со стоп-словами
string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."

# lambda-функция, фильтрующая стоп-слова
split_str = string_to_process.split()
filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))

print("Отфильтрованная строка:a", filtered_str)