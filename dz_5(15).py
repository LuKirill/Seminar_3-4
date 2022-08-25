# -Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]
my_list = []
n = int(input("Введите число n: "))
f = 1
for i in range(1, n + 1):
    f *= i
    my_list.append(f)
print(my_list)