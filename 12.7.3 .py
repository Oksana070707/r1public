per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a= per_cent.get('ТКБ')
b = per_cent.get('СКБ')
c = per_cent.get('ВТБ')
d = per_cent.get('СБЕР')
money = int(input('Введите сумму вклада (рублей):'))
e = money
A = e * a/100
B = e * b/100
C = e * c/100
D = e * d/100
deposit = [A, B, C, D]

print(list(map(int, deposit)))
print(max(deposit))