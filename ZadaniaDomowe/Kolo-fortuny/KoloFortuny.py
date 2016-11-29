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

    def __init__(self):
        self.hasla = []
        self.kategorie = []
        self.wylosowaneHaslo = ""
        self.liczba = 0

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
        return random.randint(1, self.liczba - 1)


class Rozgrywka:

    def __init__(self, koloObs):
        self.czy_odgadniete = False
        self.liczba_pkt = []
        self.kolo = koloObs
        for x in range(1, self.kolo.liczba + 1):
            self.liczba_pkt.append(1)

    def gra(self):
        random.seed()
        uczestnik = self.kolo.losuj_pierwszego()
        pozostale_litery = len(self.kolo.wylosowaneHaslo)
        print "zaczyna gracz: " + str(uczestnik)
        print "haslo ma " + str(pozostale_litery) + " znakow"

        while not self.czy_odgadniete:
            wylosowana_liczba = random.randint(-10, 11)
            while wylosowana_liczba != 0:
                print "wylosowano liczbe: " + str(wylosowana_liczba)
                literka = raw_input("Podaj literke\n")

                if self.kolo.wylosowaneHaslo.__contains__(literka):
                    pozostale_litery -= 1
                    if wylosowana_liczba > 0:
                        self.liczba_pkt[uczestnik] += wylosowana_liczba
                    odp = raw_input("Dobra robota, teraz odgadnij haslo\n")

                    if str(self.kolo.wylosowaneHaslo).strip() == str(odp):
                        print "Gratulacje!!"
                        self.liczba_pkt[uczestnik] = self.liczba_pkt[uczestnik] * pozostale_litery
                        self.czy_odgadniete = True
                        break
                else:
                    self.liczba_pkt[uczestnik] = 0

                wylosowana_liczba = random.randint(-10, 11)

            uczestnik = (uczestnik % self.kolo.liczba) + 1

    def pkt_do_pliku(self):
        plik = open("punkty.txt","wb")
        for pkt in self.liczba_pkt:
            plik.writelines(str(pkt) + ", ")

obsluga = ObslugaKola()
obsluga.wczytaj_liczbe_uczestnikow()
obsluga.wczytaj_hasla()
obsluga.wczytaj_kategorie()
obsluga.losuj_haslo()

rozgrywka = Rozgrywka(obsluga)
rozgrywka.gra()
rozgrywka.pkt_do_pliku()
