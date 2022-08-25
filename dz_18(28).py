# Найти корни квадратного уравнения Ax² + Bx + C = 0
# a)Математикой
# b)Используя дополнительные библиотеки*

# a)
a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет")
    quit()
elif d == 0:
    x1 = -b / 2 * a
    print(f'{x1:.2f}')
    quit()
else:
    x1 = (-b + d ** 0.5)/2 * a
    x2 = (-b - d ** 0.5)/2 * a
    print(f'{x1:.2f}, {x2:.2f}')

# b)
import math
import sys
a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))
d = math.pow(b, 2) - 4 * a * c
if d < 0:
    print("Корней нет")
    sys.exit()
elif d == 0:
    x1 = -b / 2 * a
    print(f'{x1:.2f}')
    sys.exit()
else:
    x1 = (-b + math.sqrt(d))/2 * a
    x2 = (-b - math.sqrt(d))/2 * a
    print(f'{x1:.2f}, {x2:.2f}')