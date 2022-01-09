# Дано: целое число
# Задача - найти количество разрядов числа

x = 100_000_000
count = 1
x //= 10

while x > 0:
    x //= 10
    count += 1
print(f'количество разрядов: {count}')

# Дано: положительное целое число
# Задача - найти факториал числа

x = 7

factorial = 1
for i in range(2, x + 1):
    factorial *= i
print(f'факториал числа {x}: {factorial}')

# Дано: список чисел
# Задача - вывести на экран все числа, которые больше среднего значение по списку

input_list = [1, 6, 13, 76, 44, 56, 12, 13, 7, 8, 9]

new_list = []

average_number = sum(input_list) / len(input_list)

for num in input_list:
    if num > average_number:
        new_list.append(num)
print(f'числа больше среднего значение: {new_list}')

# Дано список ключей и соответствующих им значений в другом списке
# Задача - объединить ключи и значения в словарь

keys_list = ['a', 'b', 'c', 'd', 'e']
values_list = [1, 2, 3, 4, 5]

dictionary = {}

for key in range(len(keys_list)):
    dictionary[keys_list[key]] = values_list[key]
print(dictionary)

# Дано: строка, содержащая предложение
# Задача - создать словарь, в котором для всех слов кроме "the" ключем будет само слово,
# а значением количество букв, из которых оно состоит.

input_sentence = "the quick brown fox jumps over the lazy dog"

my_dict = {word: len(word) for word in input_sentence.split(' ') if word != 'the'}
print(my_dict)

# Дано: 3 множества чисел
# Задача - построить список из всех возможных комбинаций, сумма элементов которых больше 7.

set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {1, 5, 9}

res = [(x, y, z) for x in set1 for y in set2 for z in set3 if x + y + z > 7]
print(res)



"""
func_input = (1, 3, 6)


def add(x, y, z):
    return x + y + z


res = add(*func_input)
print(res)


def fib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = list(fib(6))
print(data)


word = 'madam'


def palidr(s):
    reverst = s[::-1]
    if s == reverst:
        return True
    return False


print(palidr(word))


def myfunc (*args):
   for item in args:
       if item%2==0:
            return item
print(myfunc(5,2,6,8))

"""