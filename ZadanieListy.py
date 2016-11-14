import random
from string import ascii_uppercase


class Zadanie1:
    lista = []
    lista2 = []
    lista_d = []

    def uzupelnij_liste(self):
        dol = input("podaj dolna granice\n")
        gora = input("podaj gorna granice\n")
        ile_elem = input("podaj liczbe elementow\n")
        random.seed()
        for ile in range(1, ile_elem):
            self.lista.append(random.randint(dol, gora))

    def wyswietl(self):
        print [x for x in self.lista]

    def wielokrotnosci(self, liczba):
        self.lista2.append([x for x in self.lista if not x % liczba]) # lista list zawierajaca wielokrotnosci dowolnej liczby

    def duplikaty_z_list(self):
        for i in self.lista2:
            temp = [x for x in i if i.count(x) > 1]
            seen = set()
            for j in temp:
                if j not in seen:
                    self.lista_d.append(j)
                    seen.add(j)

    def zastap_duplikaty(self):
        self.lista_d = map(lambda x: 'X' if self.lista_d.count(x) > 1 else x, self.lista_d)

    def usun_duplikaty(self):
        self.lista = map(lambda x: self.lista.pop(self.lista.index(x)) if self.lista.count(x) > 1 else x, self.lista)

    def srednia_z_listy(self):
        return reduce(lambda x, y: x + y, self.lista)/self.lista.__len__()

    def podnies_do_potegi(self, liczba):
        return [x**liczba for x in self.lista]

    def zastap_wielokrotnosci(self):
        self.lista = map(lambda x: 'A' if not x % 2 else 'E' if not x % 3 else 'L' if not x % 5 else x, self.lista)

    def zastap_lpierwsze(self):
        self.lista = map(lambda x: 'Z' if self.czy_pierwsza(x) else x, self.lista)

    def czy_pierwsza(self, liczba):
        if not isinstance(liczba, (int, long)):
            return False
        liczba = int(liczba)
        for i in range(2, liczba / 2):
            if liczba % i == 0:
                return False
        return True

    def generuj_napisy(self):
        znaki = [x for x in self.lista if isinstance(x, basestring)]
        for i in range(1, 10):
            print ''.join(random.choice(znaki) for j in range(znaki.__len__()))

zadanie1 = Zadanie1()
zadanie1.uzupelnij_liste()
zadanie1.wyswietl()
zadanie1.wielokrotnosci(2)
zadanie1.wielokrotnosci(3)
zadanie1.wielokrotnosci(5)
zadanie1.duplikaty_z_list()
zadanie1.zastap_duplikaty()
zadanie1.usun_duplikaty()
print zadanie1.srednia_z_listy()
print zadanie1.podnies_do_potegi(3)
zadanie1.zastap_wielokrotnosci()
zadanie1.zastap_lpierwsze()
zadanie1.generuj_napisy()
