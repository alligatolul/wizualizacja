import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# df = pd.DataFrame(ts, columns=['wartosci'])
# df['Średnia krocząca'] = df.rolling(window=50).mean()
# df.plot()
# plt.legend()
# plt.show()

# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartosci')
# plt.ylabel('Prawdopodobienstwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()


# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges, texts, autotext = plt.pie(x=seria, labels=seria.index,
#                                   autopct=lambda pct: "{:.1f}".format(pct),
#                                   textprops=dict(color='black'),
#                                   colors=['red','green'])
# plt.title('Suma zamówień dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()

#zad1

# x = np.arange(1,21)
# y = 1/x
# plt.plot(x, y, 'g', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.axis([1,len(x),0,1])
# plt.show()

#zad2

# x = np.arange(1,20)
# y = 1/x
# plt.plot(x, y, 'g:^', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend()
# plt.axis([0,20,0,1])
# plt.show()

#zad3

# x = np.arange(0, 30.1, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# plt.plot(x, y1, 'g', label='sin(x)')
# plt.plot(x, y2, 'm', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('wartosci')
# plt.legend(loc='upper right')
# plt.show()


sns.set()
# wykres 1

# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 8, 16], label='linia nr1',
#              color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 9, 17], label='linia nr1',
#              color='green', marker='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Wykres liniowy')
# plt.show()

# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii',)
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('Wykres liniowy')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartosci')
# wykres.add_legend()
#
# plt.show()

# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')

# sns.lineplot(data=df, x=df.index, y='sepal length', hue='class',
#              palette=['magenta', 'blue', 'green'])
# plt.xlabel('indeksy')
# plt.ylabel('sepal length')
# plt.title('dane z iris database')
# plt.show()

# data={'a': np.arange(10), 'c': np.random.randint(0, 50, 10),
#       'd': np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# df = pd.DataFrame(data)
#
# plot = sns.relplot(data=df, x='a', y='b', hue='c', palette='bright', size='d',
#                    legend=True)
# plot.set(xticks=data['a'])
# plt.show()


data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południwa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)

plot = sns.barplot(data=df, x='Kontynent', y='Populacja', hue='Kontynent',
                   estimator=np.sum, dodge=False, palette=['red', 'green', 'blue'],
                   errorbar=None)
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()
