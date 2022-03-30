def sim_calc():
    x = float(input("Enter the nuber of hours worked:"))  # Введите количество отработанных чвсов
    y = float(input("Enter the amount of remune ratio in 1 hour:"))   # Введите сумму оплаты труда за 1 час
    c = float(input("Specify the size of the prize:"))   # Укажите размер премии
    pay = x * y
    return pay + c
print(f"The amount of salary: {sim_calc()}")  # Размер зарплаты составил

