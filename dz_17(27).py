# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

my_str = input("Введите строку из чисел: ")
min_num = min(list(my_str))
max_num = max(list(my_str))
print(min_num, max_num)