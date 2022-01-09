# Написать функцию, которая принимает неограниченное количество
# аргументов и возвращает максимальный четный аргумент

def max_even_element(*args):
    return max([max_num for max_num in args if max_num % 2 == 0])


print(max_even_element(3, 4, 6, 121, 13, 42))

# Написать функцию, которая как аргумент принимает имя (текстом) одной из 4-х арифметических операций
# (сумма, сложение, вычитание, деление) и возвращает другую функцию, которая выполняет эту операцию для 2х переменных


def func_factory(operations):
    if operations == 'sum':
        def sum(x, y):
            return x + y
        return sum
    elif operations == 'mul':
        def mul(x, y):
            return x * y
        return mul
    elif operations == 'sub':
        def sub(x, y):
            return x - y
        return sub
    elif operations == 'div':
        def div(x, y):
            return x / y
        return div


adds = func_factory('sum')
print(adds(1, 5))

muls = func_factory('mul')
print(muls(3, 6))

divs = func_factory('div')
print(divs(9, 3))

# Используя функцию из предыдущей задачи создать список из полученных функций
# (выполняющих арифметические операции) и применить их по очереди к одной и той же паре аргументов

magic_list = [func_factory('sum'), func_factory('mul'), func_factory('sub'), func_factory('div')]

for funk in magic_list:
    print(funk(6, 3))

