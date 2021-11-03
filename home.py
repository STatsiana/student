a = input('Enter: ')
b = input('Enter: ')
try:
    int(a)
    int(b)
    a = int(a)
    b = int(b)
    if a in range(3,21):
        if a - b > 0:
            c = int(a - b)
        else:
            c = int(b - a)
    if b in range(3,21):
        if a - b > 0:
            c = int(a - b)
        else:
            c = int(b - a)
    else:
        a = str(a)
        b = str(b)
        c = a + b
except ValueError:
    try:
        float(a)
        float(b)
        a = float(a)
        b = float(b)
        if a in range(3,21):
            if a - b > 0:
                c = float(a - b)
            else:
                c = float(b - a)
        if b in range(3,21):
            if a - b > 0:
                c = float(a - b)
            else:
                c = float(b - a)
        else:
            a = str(a)
            b = str(b)
            c = a + b
    except ValueError:
        c = a+b


print(c)


