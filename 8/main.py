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


x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(4, 1, 1)
plt.plot(x1, y1, 'm')
plt.title('Wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.subplot(4, 1, 4)
plt.plot(x2, y2, 'g')
plt.title('Wykres cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.subplots_adjust(hspace=0.5)
plt.show()


