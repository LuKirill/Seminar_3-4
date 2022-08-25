# Дано число. Составить список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так:
#  [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

fib_list = []
n = int(input())
fib1 = fib2 = 1
negafib1, negafib2 = 1, -1
fib_list.append(negafib2)
for j in range(-1, -n + 1, -1):
    negafib1, negafib2 = negafib2, negafib1 - negafib2
    fib_list.insert(0, negafib2)
fib_list.append(0)
fib_list.append(fib1)
fib_list.append(fib2)
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    fib_list.append(fib2)
print(fib_list)