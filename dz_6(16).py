# -Задать список из n чисел последовательности (1+1/n)**n и вывести на экран их сумму
n = int(input("Введите число n: "))
my_list = []
my_list1 = []
for n in range(1, n + 1):
    my_list.append(n)
    for i in my_list:
        my_list1.append((1 + 1 / i) ** i)
total = sum(my_list1)
print(my_list)
print(total)
