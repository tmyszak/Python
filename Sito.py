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
n = input("Podaj n\n")
sito_lista = sito(n)
for i in range(0, len(sito_lista)):
    print sito_lista[i],