# -*- coding: utf-8 -*-
import random

l = range(1, 21, 2)
print l

print [2 * x for x in l]

print [(x, x * x) for x in range(1, 5)]

print [(x, ord(x)) for x in "ABCDEF"]

print [[] for x in range(10)]

print "--------------------------------------------"
#prosta warunkowa
print [x for x in l if x > 10]

print [x for x in range(1, 20) if not x % 3 or not x % 5]

print [(x, ord(x)) for x in "ABCDEF" if x in "AEIOUY"]

#rozszerzona warunkowa
print [(x, y) for x in range(1, 5) for y in range(4, 0, -1)]

print [x - y for x in range(1, 5) for y in range(4, 0, -1)]

print [`x` + y + `z` for x in [1, 2] for y in ['A', 'B'] for z in [0, 3]]

print [(x, y) for x in range(1, 5) for y in range(6, 3, -1) if x < y]

print [(x, y) for x in range(1, 5) for y in range(6, 3, -1) if x + y < 7]

#pierwszy parzysty(x), drugi nieparzysty(y)
print [(x, y) for x in range(1, 5) for y in range(6, 2, -1) if not (x % 2) or (y % 2)]

print [(x, y) for x in range(1, 5) if not (x % 2) for y in range(6, 2, -1) if (y % 2)]

# ----------------------------------------------------------

print "-----------------------------------------------------"

dziel = lambda x, y, z: (x + y) / z

print dziel(7, 4, 6)

# wywolanie funkcji z parametrami uzyskanymi z rozpakowania sekwencji
xyz = (7, 4, 6)
print apply(dziel, xyz)

#wywoluje okreslona funkcje dla kazdego elementu sekwecji z osobna
print map(lambda x: x * x * x, range(10))
print map(dziel, range(10), range(10), [2] * 10)

print "-------------------------------zip-------------------------------"
print zip("abcdef", [1, 2, 3, 4, 5, 6])
print zip(range(1, 10), range(9, 0, -1))
print zip("zip", range(0, 9), zip(range(0, 9)))

print "-------------------------filter-----------------------------------"
samogloska = lambda x: x.lower() in "aeiou"
print samogloska('A')
print filter(samogloska, "ala ma kota")

print filter(lambda x: not samogloska(x), "Ala ma kota")

#agregowanie danych, operacja obliczania pojedynczego wyrazenia zaleznego od wszystkich elementow listy zrodlowej
print "-----------------------reduce-------------------------------"

print reduce(lambda x, y: x + y, [1, 2, 3])

print reduce(lambda x, y: x+y, map(lambda x: x * x, range(1, 3)))

# ----------------------------------------------------------------------------------------------

print
print


class Zadanie1:
    lista = []
    lista2 = []
    lista_d = []

    def uzupelnij_liste(self):
        dol = input("podaj dolna granice")
        gora = input("podaj gorna granice")
        random.seed()
        for ile in range(1, 10):
            self.lista.append(random.randint(dol, gora))

    def wyswietl(self):
        print [x for x in self.lista]

    def wielokrotnosci(self, liczba):
        self.lista2 = [x for x in self.lista if not x % liczba]
        print [x for x in self.lista2]

    def duplikaty_z_list(self):
        self.lista_d = [x for x in self.lista2]
        print [x for x in self.lista_d]

    # def zastap_duplikaty(self):
       # self.lista.


zadanie1 = Zadanie1()
zadanie1.uzupelnij_liste()
zadanie1.wielokrotnosci(2)
zadanie1.duplikaty_z_list()

