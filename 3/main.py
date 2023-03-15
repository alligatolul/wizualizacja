import random
import math
#zad 1

A = [1-x for x in range(1, 11)]
print(A)
B = [4**x for x in range(8)]
print(B)
C = [x for x in B if x % 2 == 0]
print(C)

#zad 2

listy1 = [random.randint(1, 10000) for x in range(10)]
listy2 = [x for x in listy1 if x % 2 == 0]
print(listy2)

#zad 3

produkty = {'jajka': 'sztuki', 'mleko': 'l', 'maka': 'kg', 'ryz': 'kg', 'woda': 'l', 'slodycze': 'sztuki',
            'ciastka': 'sztuki'}
prod = [x[0] for x in produkty.items() if x[1] == 'sztuki']
print(prod)

#zad 4

def czyprostokatny(a, b, c):
    if a > b and a > c and b*b+c*c == a*a:
        print("Jest prostokatny")
    elif b > a and b > c and a*a+c*c == b*b:
        print("Jest prostokatny")
    elif c > b and c > a and b*b+a*a == c*c:
        print("Jest prostokatny")
    elif a==b and a<c and b*b+a*a == c*c:
        print("Jest prostokatny")
    elif c==a and c < b and a*a+c*c == b*b:
        print("Jest prostokatny")
    elif c==b and c < a and b*b+c*c == a*a:
        print("Jest prostokatny")
    else:
        print("Nie jest prostokatny")
czyprostokatny(3, 4, 5)
czyprostokatny(9, 3, 2)

#zad 5
def poletrapezu(a = 2, b = 3, h = 4):
    return ((a+b)*h)/2
print(poletrapezu())
print(poletrapezu(4, 5, 6))

#zad 6

def dziwne(a = [1], b = 4, ile = 10):
    if ile > len(a):
        ile = len(a)
    for i in range(ile):
        a[i] = a[i] * b
    return a
print(dziwne())

#zad 7



#zad 8



#zad 9

li = int(input("podaj liczbe to pierwiastka"))

try:
    print(math.sqrt(li))
except ValueError:
    print("liczba ujemna")

