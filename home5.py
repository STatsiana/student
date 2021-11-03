x = int(input('введите число: '))
sum = 0

while x>0:
    n = x % 10
    sum = sum + n
    x = x//10


print(sum)


