n = int(input("Введите количество билетов: "))
price = 0# счётчик
for i in range(n):
    age = int(input("Возраст: "))
    if age < 18:
        price += 0
    elif 18 <= age < 25:
        price += 990
    else:
        price += 1390
if n > 3:
    f = 0.9
else:
    f = 1
print("К оплате:", price * f, "руб.")
