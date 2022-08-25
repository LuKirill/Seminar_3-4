# Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6]
my_list = [2, 3, 5, 6]
revers_list = my_list[::-1]
n = len(my_list)
if n % 2 != 0:
    a = n // 2 + 1
elif n % 2 == 0:
    a = n // 2
my_list = my_list[:a]
revers_list = revers_list[:a]
total_list = [x * y for x, y in zip(my_list, revers_list)]
print(total_list)