'''
from Tkinter import *
root = Tk()
w = Label(root, text="label")
r = Button(root, text="przycisk")
w.pack()
r.pack()
root.mainloop()
'''

# -----------------------------------------------------------------------------------
'''from Tkinter import *


class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.pack(expand=YES, fill=BOTH)
        self.master.title("Tytul")

        self.button = Button(self, text="Quit", fg="red", command=self.quit1, width=16, height=1)
        self.hi_there = Button(self, text="Hej", command=self.say_hi, width=16, height=1)

        self.Label1 = Label(self, text="Etykieta tekstowa")
        self.Label2 = Label(self, text="Etykieta tekstowa z ikona")
        self.Label3 = Label(self, bitmap="warning")

        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack()
        self.Label2.pack()
        self.Label3.pack()

    def quit1(self):
            print "Koniec"
            quit()

    def say_hi(self):
        print "Czesc"


def main():
    LabelDemo().mainloop()

if __name__ == "__main__":
    main()
'''
# -----------------------------------------------------------------------------------
'''import Tkinter


class App:
    def __init__(self, master):
        Tkinter.Button(master, text="Przycisk1").pack(side=Tkinter.TOP)
        Tkinter.Button(master, text="Przycisk2").pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="Przycisk3").pack(side=Tkinter.RIGHT)


root = Tkinter.Tk()
root.option_add("*font", ("verdana", 12, "bold"))
root.title(u"przyk\u0142ad geometrii pack")
display = App(root)
root.mainloop()
'''
# ----------------------------------------------------------------------------------
'''from Tkinter import *


class Fib(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.string = ""
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Tytul")

        self.button = Button(self, text="Oblicz", fg="black", command=self.oblicz, width=16, height=1)
        self.Label = Label(self, text=self.string)

        self.button.pack()
        self.Label.pack()

    def oblicz(self):
        a = 0
        b = 1
        n = 20
        i = 1
        while i < n:
            temp = a
            a = b
            b = a + temp
            i += 1
            self.string += str(b) + " "

        self.Label = Label(self, text=self.string)
        self.Label.pack()


def main():
    Fib().mainloop()

if __name__ == "__main__":
    main()'''

from Tkinter import *


class Calc(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.string = ""
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Tytul")

        self.button1 = Button(self, text="1", fg="black", command=lambda: self.przycisk("1"), width=16, height=1)
        self.button2 = Button(self, text="2", fg="black", command=lambda: self.przycisk("2"), width=16, height=1)
        self.button3 = Button(self, text="3", fg="black", command=lambda: self.przycisk("3"), width=16, height=1)
        self.button4 = Button(self, text="4", fg="black", command=lambda: self.przycisk("4"), width=16, height=1)
        self.button5 = Button(self, text="5", fg="black", command=lambda: self.przycisk("5"), width=16, height=1)
        self.button6 = Button(self, text="6", fg="black", command=lambda: self.przycisk("6"), width=16, height=1)
        self.button7 = Button(self, text="7", fg="black", command=lambda: self.przycisk("7"), width=16, height=1)
        self.button8 = Button(self, text="8", fg="black", command=lambda: self.przycisk("8"), width=16, height=1)
        self.button9 = Button(self, text="9", fg="black", command=lambda: self.przycisk("9"), width=16, height=1)
        self.buttonplus = Button(self, text="+", fg="black", command=lambda: self.przycisk("+"), width=16, height=1)
        self.buttonminus = Button(self, text="-", fg="black", command=lambda: self.przycisk("-"), width=16, height=1)
        self.buttonmnoz = Button(self, text="*", fg="black", command=lambda: self.przycisk("*"), width=16, height=1)
        self.buttondziel = Button(self, text="/", fg="black", command=lambda: self.przycisk("/"), width=16, height=1)
        self.buttonwynik = Button(self, text="=", fg="black", command=self.oblicz, width=16, height=1)

        self.Podglad = Label(self, text=self.string)
        self.Label = Label(self, text=self.string)

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
        self.buttonplus.grid(row=0, column=3)
        self.buttonminus.grid(row=1, column=3)
        self.buttonmnoz.grid(row=2, column=3)
        self.buttondziel.grid(row=3, column=0)
        self.buttonwynik.grid(row=3, column=1)

        self.Label.grid(row=4, column=0)

    def przycisk(self, arg):
        self.string += arg
        self.Podglad.pack_forget()
        self.Podglad = Label(self, text="Dzialanie: " + self.string)
        self.Podglad.grid(row=4, column=0)

    def oblicz(self):
        wynik = eval(self.string)
        self.Label.pack_forget()
        self.Label = Label(self, text="Wynik: " + str(wynik))
        self.Label.grid(row=5, column=0)


def main():
    Calc().mainloop()

if __name__ == "__main__":
    main()

