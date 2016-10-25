'''import random
A = set([1, 2, 3])
print A

A.discard(3)
print A

A.add(5)
print A

B = frozenset([5, 6, 4])
print B

dictionary = {8, 9}
print dictionary

C = set([4, 1, 2])
C.add(B)
print C

D = set()
print D

print len(A), len(B), len(C), len(D)

print 5 in A, 5 in B, 5 in C, 5 in D

print 8 not in A, 8 not in B, 8 not in C, 8 not in D
print "\n"

#podzbior
print set([1,2]) <= A
print set([3,4]) <= B
print set([5]) <= C
print set([1,3,5]) <= D

print A.issubset(B)
print

#nadzbior
print A >= set([1,2])
print B >= set([3,4])

print A.issuperset(B)
print

#suma
E = A | B
print E
print

#iloczyn
F = A & B
print F
print

print A - B
print B - A
print

#roznica symetryczna
G = A ^ B
print G

# ------------------------------------------------------------------


class Napis:
    txt = "pierwsza klasa"

    def wyswietl(self):
        return "czesc"

napis = Napis()

print napis.wyswietl

print napis.txt


class Zespolona:
    def __init__(self, rzeczywista, urojona):
        self.r = rzeczywista
        self.i = urojona

x = Zespolona(5.0, -3.2)
print x.r, x.i

# ------------------------------------------------------------------

napis = "witaj w swiecie PYTHONA!"

print napis.capitalize()
print napis.center(64)
print napis.center(64, '*')
print napis.count('e')
print napis.find("Taj")
print napis.find("taj")
print napis.isdigit()
print '12'.isdigit()
print '12.4'.isdigit()
print ' '.join(['Python', 'jest', 'super'])
print napis.join(['****'] * 5)
print napis.lower()
print napis.replace('PYTHONA', 'programowanie')
print napis.rfind('PYTHONA')
print 'Python jest super'.rfind('e')
print napis.rjust(32)
print napis.rjust(64)
print napis.rjust(64,'.')
print napis.split()
print '123-456-789'.split('-')
print ((napis + '\n') * 10).splitlines()
print napis.swapcase()
print napis.title()
print napis.upper()

# -------------------------------------------------------------------

l = range(1, 21)
print l

l.append(22)
print l

l.extend([20, 24])
print l

print l.count(20)
# print l.index(28)

l.insert(12, 44)
print l

l.pop(12)
print l

l.remove(20)
print l

l.sort()
print l

# -----------------------------------------------------------------------------
print "----------------------------------"
random.seed()
print random.randint(1, 15)
print random.randint(1, 15)

l = range(1, 10)
print random.choice(l)

random.shuffle(l)
print l

print random.random()

print random.uniform(10, 30)

print random.normalvariate(5, 48)  # rozklad normalny o sredniej 5 i odchyleniu 48

# -----------------------------------------------------------------------------

print "--------------------------------------------"


class Adres:
    pass

adr1 = Adres()
adr1.ulica = "Stonogi"
adr1.nr = 23
adr1.kod = '64-345'
adr1.miasto = 'Dno'

print adr1.ulica
print adr1.__dict__

# ----------------------------zadanie 1-------------------------------------------------

print "-----------------------------------------------"

random.seed()
a = input("Podaj dolna granice: \n")
b = input("Podaj gorna granice: \n")

c = random.randint(a, b)

d = input("zgadnij liczbe:\n")

while d != c:
    s = (a+b) / 2
    if s < d:
        print "liczba jest mniejsza"
    else:
        print "liczba jest wieksza"

    d = input("zgadnij liczbe:\n")

print "brawo"
'''

osoby = []


class Ksiazka_Adresowa:

    def dodaj_osobe(self):
        imie = raw_input("Podaj imie: ")
        nazwisko = raw_input("Podaj nazwisko: ")
        adres = raw_input("Podaj adres: ")
        pesel = raw_input("Podaj pesel: ")
        osoba = Osoba(adres, imie, nazwisko, pesel)
        osoby.append(osoba)

    def wyswietl_osoby(self):
        print "%20s %20s %20s %20s" % ("imie", "nazwisko", "adres", "pesel")
        for line in osoby:
            print "%20s %20s %20s %20s" % (line.imie, line.nazwisko, line.adres, line.adres)

    def edycja(self):
        a = raw_input("podaj pesel osoby, ktora chcesz edytowac: ")
        b = raw_input("podaj pole, ktore chcesz edytowac: ")
        self.edytuj_osobe(a, b)

    def edytuj_osobe(self, pesel, pole):
        for line in osoby:
            if pesel == line.pesel:
                a = raw_input("podaj nowa wartosc pola: ")
                if pole == "imie":
                    line.imie = a
                elif pole == "nazwisko":
                    line.nazwisko = a

    def usuwanie_osobe(self, pesel):

class Osoba:

    def __init__(self, adres, imie, nazwisko, pesel):
        self.adres = adres
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel


ksiazka = Ksiazka_Adresowa()
ksiazka.dodaj_osobe()
ksiazka.wyswietl_osoby()

