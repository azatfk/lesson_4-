import random
list = []
for i in range(30):
    list.append((random.randint(0, 10)))
print(list)

j = 0
list = [i*j for i in range(0, 4) if j in range(0, 4)]
print("Source list items: \n", list)   # Исходный элементь списка
nev_list = [i for i in list if list.count(i) == 1]
print("List items that don't have repetitions:\n", nev_list)   # Элементы списка не имеющий повторений
