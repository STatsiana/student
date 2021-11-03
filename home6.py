a = int(input('введите число a:'))
b = int(input('введите число b:'))


while a != b :
    if a > b:
        a = a - b

    else:
        b = b - a

print(a)

