a = input('Enter: ')
b = input('Enter: ')
c = input('Enter: ')

try:
    int(a)
    int(b)

    a = int(a)
    b = int(b)

    a = range(3,23)
    b = range(3,23)

except ValueError:
    print('Error')

print(а, c, b)


