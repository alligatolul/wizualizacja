import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# x = np.array([1, 2, 3, 4])
# y = x**2
#
# plt.plot(x, y, 'c-', label='cyan')
# plt.plot(x, y*2, 'b--', label='blue')
# plt.plot(x, y*3, 'g:', label='green')
# plt.legend()
# plt.xlabel('nie wiem')
# plt.ylabel('tego tez nie')
# plt.title('kolory chyba')
# plt.savefig('wykres1.png')
# plt.show()
#
# img = Image.open('wykres1.png')
# img = img.convert('RGB')
# img.save('wykres.jpg')

# wykres liniowy sinus na przedziale dla x<0, 10> z krokiem 0.1

# x = np.arange(0, 10.01, 0.1)
# y = np.sin(x)
#
# plt.plot(x, y, 'c-', label='sinus')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('sin x')
# plt.title('sinus dla x <0,10>')
# plt.show()


# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 150, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 *np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='seismic')
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()


# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)

# plt.subplot(4, 1, 1)
# plt.plot(x1, y1, 'm')
# plt.title('Wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2, 'g')
# plt.title('Wykres cos(x)')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, 'g:')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'k-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('Wykres cos(x)')
#
# axs[2, 0].plot(x1, y1, 'm--')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('sin(x)')
# axs[2, 0].set_title('Wykres sin(x)')
#
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
#
# plt.show()


data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południwa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
#
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
#
# plt.bar(etykiety, wartosc, color=['cyan', 'gray', 'green'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja w mld')
# plt.title('Wykres populacji w kilku krajach')
# plt.show()


# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
# # grupa.plot(kind='bar', xlabel='kontynent', ylabel='wartosci w mld', legend=True,
# #             title='Populacja na kontynentach', rot=0)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('kontynent')
# wykres.set_ylabel('ilosc')
# wykres.tick_params(axis='x', labelrotation=0)
# wykres.legend()
# wykres.set_title('title')
# plt.show()
