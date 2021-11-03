a = int(input('введите размер вклада: '))
years = int(input('введите срок вклада: '))

def bank():
    stavka = 10
    cash = (a + a * stavka // 100) * years
    print(cash)

bank()

