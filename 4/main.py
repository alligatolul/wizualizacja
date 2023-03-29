
# zad 1

# A = [i*2 for i in range(0, 31)]
# plik = open("nazwa1.txt", "w+")
#
# plik.writelines(str(A))
# plik.close()

# zad 2
# plik = open("nazwa1.txt", "r")
#
# print(plik.readlines())
# plik.close()

#zad 3


# with open("nazwa2.txt", "w+") as plik:
#     plik.writelines("kilka dziwnych linjek do zrobienia \n")
#     plik.writelines("lorem ipsum i takie tam \n")
#     plik.writelines("coraz wiecej informacji \n")
#
# with open("nazwa2.txt", "r") as plik:
#     for x in plik:
#         print(x, end="")

# zad 4

class naZakupy:

    def __init__(self, nazwa_produktu, cena_jed, jednostka_miary, ilosc):
        self.cena_jed = cena_jed
        self.jednostka_miary = jednostka_miary
        self.ilosc = ilosc
        self.nazwa_produktu = nazwa_produktu

    def wyswietl_produkt(self):
        print(f"nazwa produktu: {self.nazwa_produktu} ")
        print(f"cena jednostkowa: {self.cena_jed} ")
        print(f"ilosc: {self.ilosc}")

    def ile_produktu(self):
        print(f"{self.ilosc} {self.jednostka_miary} ")

    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)


# jajka = naZakupy("jajka", 3, "szt", 12)
# jajka.wyswietl_produkt()
# jajka.ile_produktu()
# jajka.ile_kosztuje()

# zad 5

class ciagi:

    def __init__(self):
        self.wartosci = []

    def wyswietl_dane(self):
        print(self.wartosci)

    def pobierz_elementy(self):
        ile = int(input("ilosc dodawanych elementow: "))
        if ile > 0:
            for i in range(ile):
                elem = float(input(f"Podaj {i + 1} element: "))
                self.wartosci.append(elem)

    def pobierz_parametry(self):
        self.pierwsza = float(input("Podaj pierwszy element: "))
        self.roznica = float(input("Podaj roznice miedzy elementami: "))
        self.ilosc_elem = int(input("podaj ilosc elementow ciagu: "))


    def policz_sume(self):
        return sum(self.wartosci)

    def policz_elementy(self):
        for i in range(self.ilosc_elem):
            self.wartosci.append(self.pierwsza + i * self.roznica)



# obiek = ciagi()
# obiek.pobierz_elementy()
# obiek.pobierz_parametry()
# obiek.policz_elementy()
# print(obiek.policz_sume())
# obiek.wyswietl_dane()
# zad 6

class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ik):
        self.y = self.y+(ik*self.krok)
    def idz_w_dol(self, ik):
        self.y = self.y-(ik*self.krok)
    def idz_w_lewo(self, ik):
        self.x = self.x-(ik*self.krok)
    def idz_w_prawo(self,ik):
        self.x = self.x+(ik*self.krok)
    def pokaz_gdzie_jestes(self):
        print(f"pozycja x to {self.x}, a  pozycja y to {self.y}")

# robak = robaczek(0, 0, 2)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_prawo(10)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_dol(13)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_lewo(5)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_gore(13)
# robak.pokaz_gdzie_jestes()