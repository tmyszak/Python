# ---------- pliki ---------------

# utworzenie i otwarcie do zapisu pliku
fl = open("plik1.txt", "wb")

print fl.name

# tryb okresla tryb w jakim otwarto plik
print fl.mode

# czy plik jest zamkniety
print fl.closed

# ---------------- metody do obslugi pliku ------------------------------

# write zapisuje do pliku napis
fl.write("Pierwszy plik")

# zapisuje dane z bufora do pliku
fl.flush()

fl.write("\nNowa linia")

# zapisuje dane z bufora do pliku i zamyka plik
fl.close()

# otwarcie pliku do modyfikacji
fl = open("plik1.txt","r+b")

# odczytuje napis z pliku
print fl.read()

# podaje aktualna pozycje w pliku
print fl.tell()

# ustawia pozycje w pliku na podana
fl.seek(0)

# nadpisuje zawartosc pliku
fl.write("Nowy poczatek")

# przesuniecie na wzgledna pozycje pliku
fl.seek(-14, 1)

# wczytanie fragmentu zawartosci pliku o okreslonej dlugosci
print fl.read(14)

# zapisuje do pliku sekwencje napisow
fl.writelines(["\n3 linia", "\n4 linia", "\n5 linia"])

# wczytuje z pliku sekwencje napisow
fl.seek(0)
print fl.readlines()

# skraca plik na podeanej pozycji
fl.truncate(30)
fl.seek(0)
print fl.read()

# zwraca True jesli plik jest dolaczony do urzadzenia terminalowego
print fl.isatty()

import sys
print sys.stdout.isatty()

# przyklad przekierowania wewnatrz programu
ekran = sys.stdout
sys.stdout = open("wyjscie.txt", "w")
print "Jestem tutaj"
print "Gdzie Ty poszedles"
sys.stdout = ekran
print open("wyjscie.txt", "r").read()
