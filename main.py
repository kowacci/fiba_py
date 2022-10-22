a = 1
b = 1

n = int(input('Введите число n:'))

i = 0
while i < n - 2:
    c = a + b
    a = b
    b = c
    i = i + 1

print('Полученное число', b)

