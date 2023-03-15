import math

#zad 1

print(math.ulp(1.0)**10)
print((math.log(5+math.sin(8)**2))**(1/6))
print(math.floor(3.55))
print(math.ceil(4.80))


#zad 2
a = "KRZYSZTOF "
b = "ZIEN"

print((a+b).capitalize())

#zad 3

tekst = "la la la la la la"

x = tekst.count("la")
print(x)

#zad 4

f = "dluga zmienna ktora nie ma znaczenia"
print(f[1], f[len(f)-1])

#zad 5

zad5 = f.split();
print(zad5)

#zad 6

flo = 6.0
txt = "jakis"
sze = hex(43)
print(f"to jest float {flo}, to jest string {txt}, to jest hex {sze}")

#zad 7

lis = ['pilka nozna', 'koszykowka', 'hokej', 'jazda na nartach']
lis.reverse()
lis.append("siatkowka")
lis.append("tennis")
print(lis)

#zad 8

dictio = {'brb': 'be right back', 'smh': 'shake my head' , 'rofl': 'rolling on floor laughing'}

print(dictio)

#zad 9

games = {'dk': 'donkey kong', 'sm': 'super mario', 'csgo': 'counter strike global offensive'}

print(len(games))

#zad 10


licz = input("podaj sentencje: ")

print(licz.count("a"))

# #zad 11

a = input("Podaj liczbe: ")
b = input("Podaj liczbe: ")
c = input("Podaj liczbe: ")

if a > b and a > c:
    print("a jest najwieksze")
elif b > a and b > c:
    print("b jest najwieksze")
elif c > a and c > b:
    print("c jest najwieksze")
elif a == b and a > c:
    print("a i b sa tak samo duze")
elif a == c and a > b:
    print("a i c sa tak samo duze")
elif b == c and b > a:
    print("b i c sa tak samo duze")
else:
    print("wszystkie liczby sa takie same")

#zad 12

poteg = [4, 12, 4.9, 23, 7.5, 2.3]

for i in range(len(poteg)):
    poteg[i] = poteg[i]**2
print(poteg)

#zad 13

lis = []
a = 0
while a < 10:
    texto = input("Podaj liczbe")
    if(int(texto)%2==0):
        lis.append(int(texto))
    a += 1
print(lis)