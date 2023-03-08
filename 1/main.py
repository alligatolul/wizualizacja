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

slownik = {'a': 2, 1: 2, 4: 'ab', 1: 3}
print(slownik)
print(slownik['a'])
slownik["k"] = 'wartosc'
print(slownik)
slownik.pop('k')
print(slownik)

print(slownik.keys())
print(slownik.values())

print('a=%(zm)d' % {'zm': 12})

print('a={}, b={}'.format(12, 13))

# if warunek:
    # instrukcja1
    # instrukcja2
# elif warunek:
    # instrukcja1
    # instrukcja1
# else:
    # instrukcja1
    # instrukcja2

# a = input('podaj a: ')
# b = input('podaj b: ')
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# a = int(a)
# b = int(b)
# print(type(a))
# print(type(b))
#
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print('a jest takie samo jak b')

# x = input('Podaj x: ')
# y = input('Podaj y: ')
# x = int(x)
# y = int(y)
# if x == y:
#     print('liczby są równe')
# else:
#     print('liczby nie są równe')

# a = input('podaj a: ')
# b = input('podaj b: ')
# c = input('podaj c: ')
# d = input('podaj d: ')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# if (a > b) & (c > d):
#     print("a większe od b i c większe od d")
# else:
#     print('a jest mniejsze od b lub c jest mniejsze od d')

# for element in sekwencja:
    # instrukcje
# else:
    # instrukcja gdy pętla się skończy

# for x in range(6):
#     print(x)
# else:
#     print('koniec pętli for')
#
# for x in lista:
#     print(x)

# for x in range(0, len(lista)):
#     print(lista[x])

# while warunek:
    # instrukcje
#else:
    # instrukcje po pętli

# licznik = 0
# while licznik != len(lista):
#     print(lista[licznik])
#     licznik += 1
# else:
#     print('koniec listy')

# liste = [3, 4, 5, 1, 7, 8]
# a = int(input('Podaj liczbe: '))
# licz = 0
# while licz != len(liste):
#     if a - liste[licz] == 0:
#         print('{} - {} = 0'.format(a, liste[licz]))
#         break
#     licz += 1

liczby = [1, 2, 2, 2, 4, 5, 6]
l = 0

while l != len(liczby):
    if liczby[l] == 2:
        liczby.pop(l)
        l -= 1
    l += 1
print(liczby)