list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
list_20 = [i for i in range(20, 240) if i % 20 == 0]
list_21 = [i for i in range(20, 240) if i % 21 == 0]
print("A list of nubmers divvisible by 20 or 21 in the range [0 ,240]:", list)    # Список чисел кратное 20 и 21 в диапозоне
print("A list of nubmers divvisible by 20 in the range [0 ,240]:", list_20)   # Список чисел кратное 20 в диапозоне
print("A list of nubmers divvisible by 21 in the range [0 ,240]:", list_21)   # Список чисел кратное 21 в диапозоне
