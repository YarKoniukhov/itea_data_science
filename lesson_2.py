# Дано: длины 3х сторон треуголника - x, y, z
# Задача: проверить, может ли такой треугольник существовать
x, y, z = 3, 4, 5
if x + y > z and x + z > y and y + z > x:
    print('треугольник существует')
else:
    print('треугольник не существует')

# Дано: кортеж из 3х чисел - (a, b, c)
# Задача: найти максимальное число
task_input = (1, 2, 7)
max_num = 0
for num in task_input:
    if num > max_num:
        max_num = num
print(max_num)

# Дано: строка содержащая дату в формате ГОД-МЕСЯЦ-ДЕНЬ
# Задача: проверить, является ли год высокосным
input_date = '2019-05-23'
year = int(input_date[:4])
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Высокосный')
else:
    print('Не высокосный')

# Дано: строка, содержащая букву английского алфавита в нижнем регистре
# Задача: проверить, является ли буква гласной
input_letter = 'g'
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
if input_letter in vowels:
    print('буква гласная')
else:
    print('буква согласная')

# Дано: коэффициенты квадратного уравнения в виде кортежа (a, b, c), где
# 0=𝑎∗𝑥2+𝑏∗𝑥+𝑐
# Задача: найти корни квадратного уравнения

input_coefficients = (2, 4, 9)
a, b, c = input_coefficients[0], input_coefficients[1], input_coefficients[2]
discr = b**2 - 4 * a * c

if discr < 0:
    print('корней нет')
elif discr == 0:
    x = (-b + discr**.5) / (2 * a)
    print(f'корень: {x}')
else:
    x1 = (-b + discr**.5) / (2 * a)
    x2 = (-b - discr**.5) / (2 * a)
    print(f'есть два корня: {x1} и {x2}')