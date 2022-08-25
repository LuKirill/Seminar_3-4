# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
my_dict = {}
my_list = []
my_new_list = []
n = int(input("Введите натуральное число n: "))
for i in range(n + 1):
    my_list.append(i)
for j in my_list:
    my_new_list.append(3 * my_list[j] + 1)
for k in range(1, len(my_list)):
    my_dict[my_list[k]] = my_new_list[k]
print(my_dict)