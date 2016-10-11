'''
skrypt1
'''

a = 45
print a
b = 54
napis = "asdasd"

print str(b) + " " + napis

a, b, c = 4, 8, 9
print a, b, c

del a

a = 0O15
print a

a = 0xabc
print a

a = 0b10101010110101111111
print a

a = 3 + 5j
print a

a = 4.6
print a

napis = "To jest\" String"
print napis

napis = "Test z tabulatorem\ti znakiem\n nowego wiersza"
print napis

napis = '''napis
o wielu
wierszach
'''
print napis

print "zielone " + "jablko"

print "B" + "a" *5+"rdzo pyszne"

print "Py" "thon"

a = 4
b = '6.5'
c = repr(a) + b
print c

print 4 * 7L

print 2.5
print 2e+5
print 4.0/3.0
print 4.0//3.0
print 3.5e+4+1000000L * 2

print -2+3j
#potega
print 3j**2
print 3.2+400L/(2+2j)

a, b, c, d, e = 1, 3, 7, 4, 5
a += 2
b -= 2
c *= 2
d /= 2

print a, b, c, d, e

#imie = raw_input("Jak masz na imie? \n")
#print imie

napis = "Wiek: " + str(2222)
print napis
print napis.replace("ie", "asd")
print napis.lower()
print napis.upper()
napis = "Ta liczba %0.3f to %s" % (3.23, "liczba")
print napis
print '{0}, {1}, {2}'.format('a', 'b', 'c')

l = [1, 2, 'sdfsdf', 3.14]
print l

k = (1, 2, 'leasdasd', 3.14)
print k

print l[1]
print k[1]

print l[1:3]
print k[:-2] # od tylu

print 1 in l

l[0] = 3
print l

#k[0] = 3  -> krotek nie mozna modyfikowac
#print k

l[1:3] = ['a', 'b']

print l

macierz = [1, [1, 2, 3, 4]]
print macierz

print macierz[1][3]

macierz[1][2] = 5
print macierz

lista = [1, 2, 3]
lista2 = lista + [4, 5, 6]

print lista2

lista = [4, 6, 2, 4, 8]
lista.sort()
print lista

lista.reverse()
print lista

lista.append(6)
print lista

lista.insert(2, 10)
print lista

lista.pop()
print lista

lista.remove(4) #pierwsza napotkana wartosc 4
print lista

del lista[1:3]
print lista

slownik = {'a' : 'b', 'klucz' : 15,3 : [1, 3, 4]}
print slownik

print slownik['a']
print len(slownik)

print list(slownik.keys())

d = {}
print 'b' in d

d['b'] = 1
print d

del slownik[3]
print slownik

slownik.clear()
print slownik

a = True
b = False
print a, b

x = 4
y = 8

print x < y
print x == y
print x != y

print a or b
print a and b
print not a
print not b

a, b = 2, 3

print a + b
print a - b
print a * b
print a / b
print a % b
print a ** b

print "----------------------------------"
a = 6
b = 5
if a < 4:
    print a
elif a > 4:
    print b

for x in range(-10, 11):
    print "%+i" % x,

print "\n"

for x in range(5, 100, 10):
    print "%3i%6o%5x" % (x, x, x)

print "----------------------------------"
for x in range(5, 100, 10):
    print "%-3i%#-6o%#-5x" % (x, x, x)

print "----------------------------------"
for x in range(5, 100, 10):
    print "%3i %#4o %#04x" % (x, x, x)

print "----------------------------------"
a = [1, 2, 3, 4, 5, 6]
while a:
    a = a[:len(a) - 1]
    print a

#zadanie 1 ciag fibonacciego

a = 0
b = 1
n = 10
i = 1

while i < n:
    temp = a
    a = b
    b = a + temp
    i += 1

print b

#zadanie 2 pole trojkata

h = 4.44
a = 12

pole = 0.5 * a * h
print pole
