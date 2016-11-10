osoby = []


class Ksiazka_Adresowa:

    def dodaj_osobe(self):
        imie = raw_input("Podaj imie: ")
        nazwisko = raw_input("Podaj nazwisko: ")
        adres = raw_input("Podaj adres: ")
        pesel = raw_input("Podaj pesel: ")
        czy_istnieje = False
        for line in osoby:
            if line.pesel == pesel:
                print "osoba o podanym peselu juz istnieje"
                czy_istnieje = True

        if not czy_istnieje:
            osoba = Osoba(imie, nazwisko, adres, pesel)
            osoby.append(osoba)

    def wyswietl_osoby(self):
        print "%-40s %-40s %-40s %-40s" % ("Imie", "Nazwisko", "Adres", "Pesel")
        for line in osoby:
            print "%-40s %-40s %-40s %-40s" % (line.imie, line.nazwisko, line.adres, line.pesel)

    def edytuj_osobe(self, pesel, pole):
        for line in osoby:
            if pesel == line.pesel:
                nowa_wartosc = raw_input("podaj nowa wartosc pola: ")
                if pole == "imie":
                    line.imie = nowa_wartosc
                elif pole == "nazwisko":
                    line.nazwisko = nowa_wartosc
                elif pole == "adres":
                    line.adres = nowa_wartosc
                elif pole == "pesel":
                    line.pesel = nowa_wartosc

    def usun_osobe(self, pesel):
        for line in osoby:
            if pesel == line.pesel:
                osoby.remove(line)


class Osoba:

    def __init__(self, imie, nazwisko, adres, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.pesel = pesel

wybor = -1
ksiazka = Ksiazka_Adresowa()
osoby.append(Osoba("Robin", "Hood", "nibylandia", "12345678901"))

while wybor != 5:
    if wybor == 1:
        ksiazka.wyswietl_osoby()
    elif wybor == 2:
        ksiazka.dodaj_osobe()
    elif wybor == 3:
        pesel = raw_input("podaj pesel osoby, ktora chcesz edytowac")
        do_edycji = raw_input("jakie pole chcesz edytowac?")
        ksiazka.edytuj_osobe(pesel, do_edycji)
    elif wybor == 4:
        pesel = raw_input("podaj pesel, ktora chcesz usunac z ksiazki")
        ksiazka.usun_osobe(pesel)

    print
    wybor = input("""
    1-wyswietl ksiazke
    2-dodaj osobe
    3-modyfikuj osobe
    4-usun osobe
    5-zakoncz
    """)
