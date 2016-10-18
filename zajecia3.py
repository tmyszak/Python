def pierw(n):
    return n**0.5

print pierw(3)


def pierw2(n):
    if n >= 0:
        return n**0.5

print pierw2(4)


def pierw3(n):
    if n >= 0:
        return n**0.5
    else:
        return (-n)**0.5*1j

print pierw3(-6)


def rs(a, b):
    return a - b, a + b

print rs(8, 4)


def suma(*arg):
    s = 0
    for x in arg:
        s += x
    return s

print suma(*range(10))


for i in range(1, 11):
    print
    for j in range(1, 11):
        print "%3i" % (i*j),

print
print "--------------------------------------------------"


def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


def nww(a, b):
    return abs(a * b / nwd(a, b))


#a = input("Podaj a:")
#b = input("Podaj b")
print nww(5, 5)
print nwd(5, 5)

# pozycja pierwszego wystapienia okreslonej liczby


def poz(lista, liczba):
    return lista.index(liczba)



lis = [1,2,3,4,5,6,7,8,9,1,2,4,5,6,45]
lic = 45

print poz(lis, lic)


def sito(n):
    tab = [0]

    for i in range(0, n):
        tab.append(1)

    p = 2
    q = p * p

    for i in range(q, n):
        if tab[p] == 1:
            i = q
            while i <= n:
                tab[i] = 0
                i += p
        p += 1
        q = p * p

    wynik = []
    for k in range(2, n + 1):
        if tab[k] == 1:
            wynik.append(k)

    return wynik

print "---------------------------------"
sito_lista = sito(25)
for i in range(0, len(sito_lista)):
    print sito_lista[i],
