from itertools import count
print("<<The program calculating the factorial of a nuber>>:")   # Бесконечый интератор целых чисел, начиная с указаного целого числа
n = int(input("Enter an integer:"))   # Введите целое число
for i in count(n):
    print(i, end='')
    if i > 10:
        break
    # print("n:\n", n, end='')
