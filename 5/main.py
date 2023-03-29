import math


# arkusz a

# zad1

# a = input("podaj pierwszą liczbę całkowitą: ")
# b = input("podaj drugą liczbę całkowitą: ")
#
# try:
#     a = int(a)
#     b = int(b)
#     wynik = a*a + a*b + b*b
#     print(wynik)
# except ValueError:
#     if type(a) != int or type(b) != int:
#         print("Miały zostać podane liczby całkowite")

# zad2

# def liczenie(lista1, lista2):
#     x = len(lista1)
#     y = len(lista2)
#     lista3 = []
#
#     if x < y:
#         for i in range(y-x):
#             lista1.append(0)
#
#     elif y < x:
#         for i in range(y - x):
#             lista2.append(0)
#
#     for i in range(len(lista1)):
#         lista3.append(lista1[i]+lista2[i])
#
#     return lista3
#
# lista = [1, 2, 4, 5, 17, 21]
# listaa = [5, 4, 23, 76, 12, 12, 13, 54]
# c = liczenie(lista, listaa)
# print(c)

# zad3

# with open("tekst.txt", "a+", encoding="utf-8") as plik:
#     plik.seek(100)
#     a = plik.read(35)
#     c = []
#     licznik = 0
#     for i in range(35):
#         if a[i] == a[i].upper() and a[i].isalpha():
#             licznik += 1
#             c.append(a[i])
#
#     if len(c) == 0:
#         print("Nie ma żadnych dużych liter")
#     else:
#         print(c, "jest tyle duzych liter:", licznik)

# zad4

# liczby = [1, 12, 4, 54, 17, 74]
# a = 7
#
# licze = [x for x in liczby if x > a]
# print(licze)

# zad5

# a = ((math.e**3) + math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(round(a, 2))

# arkusz b

# zad1

# with open("tekst.txt", "r+", encoding="utf-8") as plik:
#     licznik = 0
#     plik.seek(71)
#     a = plik.read(40)
#     for i in a:
#         if i == "A":
#             licznik += 1
#     if licznik == 0:
#         print("Nie ma żadnych A w tym odcinku tekstu")
#     else:
#         print(licznik)

# zad2

# A = [1, 4.5, 23, 65, 5.6, 12.7, 21, 8.75]
#
# B = [x for x in A if type(x) == float]
#
# print(A)
# print(B)

# zad3

# def zliczenie(lista):
#     a = lista[0]
#     for i in range(len(lista)):
#         lista.append(a+lista[i])
#     return lista
#
#
# lista = [1, 2.5, 6.7, 21, 5.6, 21, 4.4]
# print(zliczenie(lista))

# zad4

# a = math.sin(56)**2 + ((4**2)/25+ math.log(85, 3))**(1/4)
# print(round(a, 2))

# zad5

# n = input("Podaj liczbę całkowitą: ")
#
# try:
#     n = int(n)
#     a = 0
#     for i in range(1, n+1):
#         a += i
#
#     with open("zadanie5.txt", "w") as plik:
#         plik.write(str(a))
# except ValueError:
#     print("n nie jest liczbą całkowitą o ile wogóle jest liczbą")
