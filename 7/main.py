import pandas as pd
import numpy as np
# zad 1

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# zad 2

# print(df[df.Liczba > 1000])

# print(df[df.Imie == "KRZYSZTOF"])

# print(sum(df.Liczba))

# print(sum(df.Liczba[df['Rok'].isin([2000,2001,2002,2003,2004,2005])]))

# print("Men:", sum(df.Liczba[df.Plec == 'M']))

# print("Women:", sum(df.Liczba[df.Plec == 'K']))

# group = df.groupby('Plec')
# k = group.get_group('K')
# men = group.get_group('M')

#nie mam pojecia


# print(men[men.Liczba == max(men.Liczba)])
# print(k[k.Liczba == max(k.Liczba)])

# zad 3

df = pd.read_csv('zamowienia.csv', header=0, decimal='.', sep=';')

# print(df.Sprzedawca.unique())

# print(df.sort_values(by='Utarg', ascending=0).head(5))

# print(df.groupby(['Sprzedawca']).agg({'Sprzedawca': ['count']}))

# print(df.groupby(['Kraj']).agg({'Utarg': ['sum']}))

# gro = df.groupby('Kraj')
# polska = gro.get_group('Polska')
# print(polska.Utarg[(polska['Data zamowienia']>'20041231') & (polska['Data zamowienia']<'20060101')].sum())

print(np.average(df.Utarg[(df['Data zamowienia'] > '20031231') & (df['Data zamowienia'] < '20050101')]))

# poddaje sie
