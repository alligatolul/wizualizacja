import numpy as np

# zad1

# a = np.array([1, 5, 6])
# b = np.array([2, 12, 7])
# c = a*b
#
# print(c)

# zad2

# a = np.array([[1,2,3], [4,5,6], [7,8,9]])
# b = np.array([[12,65,21,87], [41,5,8,43], [1,9,-2,4], [13,9,7,98]])
#
# c = b.min(axis = 0)
# d = b.min(axis = 1)
# e = a.min(axis = 0)
# f = a.min(axis = 0)
# print(c)
# print(d)
# print(e)
# print(f)

# zad3

# a = np.array([1, 5, 6])
# b = np.array([2, 12, 7])
#
# c = a.dot(b)
#
# print(c)

# zad4

# a = np.array([4, 6, 8])
# b = np.array([4.3, 6.5, 2.8])
#
# print(a*b)
# print(a.dot(b))

# zad5

# c = np.array([[2,7],[12,9],[1,0]])
# a = np.sin(c)
# print(a)
#
# #zad6
#
# d = np.array([[2,7],[12,9],[1,0]])
# b = np.cos(d)
# print(b)


# zad7


# wynik = a+b
# print(wynik)

# zad8

# zad8 = np.array([[3,6,9],[2,5,8],[1,4,7]])
#
# for i in zad8:
#     print(i)

# zad9

# zad9 = np.array([[3,6,9],[2,5,8],[1,4,7]])
# for i in zad9.flat:
#     print(i)

# zad10

# zad10 = np.array([[np.arange(9)],[np.arange(9)],[np.arange(9)],[np.arange(9)],[np.arange(9)],[np.arange(9)],
#                   [np.arange(9)],[np.arange(9)],[np.arange(9)]])
#
# print(zad10.reshape(3, 27))


# możliwości to: (3,27) (27,3), (1,81) (81,1),
# Jest ich tyle poniważ liczba musi być podzielna bez reszty

# zad11

zad11a = np.array([12, 43, 32, 87, 9, 90, 23, 21, 76, 10, 18, 81]).reshape(3,4)
zad11b = np.array([12, 43, 32, 87, 9, 90, 23, 21, 76, 10, 18, 81]).reshape(4,3)
zad11c = np.array([12, 43, 32, 87, 9, 90, 23, 21, 76, 10, 18, 81]).reshape(2,6)

print(zad11a)
print(zad11b)
print(zad11c)

print("po ravelu:")

print(zad11a.ravel())
print(zad11b.ravel())
print(zad11c.ravel())

# all the same as it used to be


