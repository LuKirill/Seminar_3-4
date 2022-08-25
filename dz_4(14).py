# -Подсчитать сумму цифр в вещественном числе.

num = int(input("Введите вещественное число: "))
num_sum = 0
while num != 0:
    num_sum += num % 10
    num = num // 10
print(num_sum)