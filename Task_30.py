# Вычислить число π c заданной точностью d Пример: при d = 0.001,π = 3.141.
# 10^(-1)  ≤  d  ≤  10^(-10)  (до 10 знаков после запятой)

import os
from math import pi
from random import*
os.system("cls")

d = randint(1, 10)
print('Точность вывода = ', d)

print('Пи = ', round(pi, d), '\n')

exit()
import math
P = 0.001
#P = float(input("Введите количество знаков после запятой для вычисления числа Пи (от 1 до 10 ):\n"))
P = str(P).split('.')
L = len(P[1])
M = str(math.pi)
print(float(M[:L+2]))
