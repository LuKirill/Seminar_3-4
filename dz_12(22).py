# Найти сумму чисел списка стоящих на нечетной позиции

a = []
b = []
for i in range(365):
    a.append(i)
for j in a:
    if a[j] % 2 != 0:
        b.append(j)
print(sum(b))