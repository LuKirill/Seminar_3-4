# В заданном списке вещественных чисел найдите разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]
float_list = [i % 1 for i in my_list]
a = max(float_list) - min(float_list)
print(int(a * 100) / 100)