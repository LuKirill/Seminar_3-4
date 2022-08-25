# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input("Введите число n-последовательности: "))
my_list = [i for i in range(n + 1)]
my_new_list = [3 ** a for a in my_list]
for id, num in enumerate(my_new_list):
    if id % 2 != 0:
        my_new_list[id] = num * -1
print(my_new_list)