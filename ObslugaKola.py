'''
Napisac skrypt, ktory bedzie dzialal jak gra w kolo fortuny.
Na poczatku gry podaje sie liczbe uczestnikow oraz losowo wybierana jest kategoria i haslo z pliku txt.
Nastepnie kazdy z uczestniow losuje liczbe od 1 do liczby uczestniow. W ten sposob ustala sie cyfry od -10 do 10.
Liczba 0 symbolizuje bankruta i kolejny uczestnik losuje.
Nastepnie podaje literke. Jesli literka znajduje sie w hasle i pkt sa ujemne to nie otrzymuje ich.
W przypadku pkt dodatnich sa dodawane sumy pkt.
Uczestnik po wylosowaniu literki ma prawo do odgadniecia hasla.
Jesli zgadnie jego pkt sa mnozone przez ilosc literek, ktore nie zostaly odkryte.
Po odgadnieciu hasla pkt wszystkich uczestnikow zapisywane sa do pliku txt
'''

import random


class ObslugaKola:
    liczba = 0
    hasla = []
    kategorie = []
    wylosowaneHaslo =""

    def wczytaj_liczbe_uczestnikow(self):
        self.liczba = input("Podaj liczbe uczestnikow\n")

    def wczytaj_hasla(self):
        with open("hasla.txt") as f:
            for line in f:
                self.hasla.append(line)

    def wczytaj_kategorie(self):
        with open("kategorie.txt") as f:
            for line in f:
                self.kategorie.append(line)

    def losuj_haslo(self):
        random.seed()
        self.wylosowaneHaslo = self.hasla[random.randint(0, self.hasla.__len__() - 1)]

    def losuj_kategorie(self):
        random.seed()
        return self.kategorie[random.randint(0, self.kategorie.__len__() - 1)]

    def losuj_pierwszego(self):
        random.seed()
        return random.randint(1, self.liczba)


class Rozgrywka:
    czy_odgadniete = False
    liczba_pkt = []

    def gra(self):
        random.seed()
        u = ObslugaKola()
        uczestnik = u.losuj_pierwszego()
        pozostale_litery = ObslugaKola.wylosowaneHaslo

        while not self.czy_odgadniete:
            wylosowana_liczba = random.randint(-10, 11)

            while wylosowana_liczba != 0:
                literka = raw_input("Podaj literke\n")

                if ObslugaKola.wylosowaneHaslo.__contains__(literka):
                    pozostale_litery -= 1
                else:
                    self.liczba_pkt[uczestnik] = 0

                if ObslugaKola.wylosowaneHaslo.__contains__(literka) and wylosowana_liczba > 0:
                    self.liczba_pkt[uczestnik] += wylosowana_liczba
                    haslo = raw_input("Zgadnij haslo\n")
                    if ObslugaKola.wylosowaneHaslo == haslo:
                        self.liczba_pkt[uczestnik] = self.liczba_pkt[uczestnik] * pozostale_litery
                        self.czy_odgadniete = True
                        break

                wylosowana_liczba = random.randint(-10, 11)

            uczestnik = (uczestnik + 1) % ObslugaKola.liczba

    def pkt_do_pliku(self):
        plik = open("punkty.txt","wb")
        for pkt in self.liczba_pkt:
            plik.write(pkt)

obsluga = ObslugaKola()
obsluga.wczytaj_liczbe_uczestnikow()
obsluga.wczytaj_hasla()
obsluga.wczytaj_kategorie()
print obsluga.losuj_haslo()
print obsluga.losuj_kategorie()

rozgrywka = Rozgrywka()
rozgrywka.gra()

