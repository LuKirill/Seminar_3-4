# Вычислить число  c заданной точностью d
# 	Пример: при d = 0.001,  pi = 3.141. 10^-1 <= d10 <= -10

k = 1
x = 0
d = int(input())
for k in range(1, 1000000):
    x = x + 4 * ((-1) ** (k + 1)) / (2 * k - 1)
print(f'{x:.{d}f}')
