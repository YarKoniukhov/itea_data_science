import numpy as np
# Написать функцию, которая принимает на вход произвольное количество матриц, проверяет можно ли их перемножить,
# и если можно, то возвращает размерность результата (можно воспользоваться циклом).

a = np.array([
    [5, 1, 1],
    [2, 8, 2]
])

b = np.array([
    [6, 3, 7, 1],
    [1, 9, 12, 9],
    [6, 3, 7, 12],
])

c = np.array([
    [1, 1, 1, 0, 0, 5, 0, 1],
    [0, 5, 0, 1, 2, 1, 3, 10],
    [2, 1, 3, 10, 0, 5, 0, 1],
    [1, 1, 1, 0, 2, 1, 3, 10],
])


def matrix(*args):
    c = []
    for mat in args:
        c.append(len(mat))
        c.append(len(mat[0]))
    while len(c) > 2:
        if c[1] == c[2]:
            del c[1:3]
        else:
            return None
    return c


print(matrix(a))

# Вычислить выражение:
# ∑𝑖=1𝑛(𝑥𝑖−𝑎𝑣𝑔(𝑥))2

x = np.array([[1, 1, 2]])

expression = np.sum(np.square(x - np.average(x)))
print(expression)

# Вывести матрицу, которая при умножении на вектор слева (Мх) приводит его к форме отклонения от среднего значения.
# То есть каждым элементом вектора-результата будет соответствующий элемент входящего вектора минус среднее значение.
# Матрица М не должна зависеть от входящего вектора х, а только от его длины. Другими словами, для создания такой
# матрицы должно быть достаточно только знания сколько в х элементов.


# Решить систему уравнений (можно воспользоваться функцией извлечения корня):
# 47𝑎2+71𝑏−2𝑐=3
# 11𝑏−8𝑐=3
# 𝑎2+𝑏+𝑐=24

vector = np.array([3, 3, 24])

matrix = np.array([
    [np.sqrt(47), 71, 2],
    [0, 11, 8],
    [np.sqrt(1), 1, 1]
])

x = np.linalg.solve(matrix, vector)
print(f'a = {x[0]}, b = {x[1]}, c = {x[2]}')

"""
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])
i = np.ones_like(v)
# i = np.ones(len(v))
# i = np.array([1, 1, 1, 1, 1, 1])

sum_thoer = np.sum(v)
sum_vector = i.dot(v)
print(sum_vector)

v = np.array([1, 2, 3, 4, 5, 6])
mean_vec = np.sum(v) / len(v)
b = np.ones(len(v)) * mean_vec
print(b)

# Написать функцию, которая принимает на вход произвольное количество матриц, проверяет можно ли их перемножить,
# и если можно, то возвращает размерность результата (можно воспользоваться циклом).


a = np.array([
    [5, 1, 1],
    [2, 8, 2]
])
# print('a-len', a.shape)

b = np.array([
    [6, 3, 7, 1],
    [1, 9, 12, 9],
    [6, 3, 7, 12],
])

c = np.array([
    [1, 1, 1, 0, 0, 5, 0, 1],
    [0, 5, 0, 1, 2, 1, 3, 10],
    [2, 1, 3, 10, 0, 5, 0, 1],
    [1, 1, 1, 0, 2, 1, 3, 10],
])


# print('m-len', m.shape)
# print('b-len', b.shape)


def matrix(*args):
    c = []
    for mat in args:
        c.append(len(mat))
        c.append(len(mat[0]))
    while len(c) > 2:
        if c[1] == c[2]:
            del c[1:3]
        else:
            return None
    return c

    # print(c)

    # if c[0][1] == c[1][0]:
    #   del c[0][1], c[1][0]
    # print(c)


# print(b.dot(a))


print(matrix(a, b, c))

# def matrix_to_mul(*args):
#   c = []
#  for i in args:
#     c.append(i.shape)
#    print('shape', i.shape)
#   print('shape[0]', i.shape[0], 'shape[1]', i.shape[1])
# print(c)

# return f'rr', c


def mat(*args):
    c = []
    for i in args:
        c.append(i.shape)
        #c.append(i.shape[1])
        print('iteration', c)
        if args.dot(args)



print(mat(a, b, c))

w = a.dot(b)
print('a.dot(b)', w)

y = w.dot(m)
print('w.dot(m)', w)

print(matrix_to_mul(a, b))



def www(*args):
    # matrix_args = np.array(args, dtype=object)
    # print(matrix_args)
    c = []
    for i in args:
        print(len(i), len(i[0]))
        c.append(len(i))
        c.append(len(i[0]))
        print(i.shape)


def t(*args):
    # args = np.array(args, dtype=object)
    c = []
    d = []
    for i in args:
        print(len(i), len(i[0]))
        print('args[0]', args[0])
        print(i)
        # print('dot', i.dot(i))
        # d.append(i)


#        c.append(len(i))
#       c.append(len(i[0]))
# print(c)

#   print()

# print(a.dot(b))


# np.append(args, len(i), len(i[0]))
# print(c)


# print(i)
# print(len(args), len(args[0]))

# print(args.shape)


# t(a, b)


# print(c)


# c.append(i.shape)

# while c[1] == c[2]:
#   del c[1:3]
#  print(c)
# for i in c:
# if c[1] == c[2]:
#      del c[1:3]
# print(c)


#   print(np.array(*args))
#    print(len(*args))

# www(a, b, c)

# Вычислить выражение:
# ∑𝑖=1𝑛(𝑥𝑖−𝑎𝑣𝑔(𝑥))2


x = np.array([[1, 1, 2]])

expression = np.sum(np.square(x - np.average(x)))

print(expression)

# Решить систему уравнений (можно воспользоваться функцией извлечения корня):
# 47𝑎2+71𝑏−2𝑐=3
# 11𝑏−8𝑐=3
# 𝑎2+𝑏+𝑐=24

vector = np.array([3, 3, 24])

matrix = np.array([
    [np.sqrt(47), 71, 2],
    [0, 11, 8],
    [np.sqrt(1), 1, 1]
])

x = np.linalg.solve(matrix, vector)
print(f'a = {x[0]}, b = {x[1]}, c = {x[2]}')
"""