# a = "napis"
# print(a)
#
# b = 5
# c = 3.2
# print(b+c)
#
# d = 5+2j
# print(d)
#
# e = c+d
# print(e)
#
# f = b//c
# print(f)
#
# g= c%b
# print(g)
#
# h = b**3
# print(h)
#
# i = b**1/2
# j = pow(b, 1/2)
# print(i)
# print(j)
#
# print('b = b + 2')
# print(b)
# b += 2
# print(b)
#
# listy = ['a', 4, 5, 6, [1, 2, 3], 5.6, ]
# print(listy)
#
# listy.append(12)
# print(listy)
#
# print(listy[2])

# dodać element na wybrane miejsce
lista = [1, 2, 65, -3, 23, 87, 42, 3, 15, 7, 19]
lista.insert(4, 13)
print(lista)

#dodać kilka elementów
lista.extend([4, 5, 6, 8])
print(lista)

# usunąć element z listy o danej pozycji
lista.pop(2)
print(lista)

# usunąć element z listy o dane wartości
lista.remove(-3)
print(lista)

# odwrócić elementy listy
lista.reverse()
print(lista)

# zrobić sortowanie
lista.sort()
print(lista)
