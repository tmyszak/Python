from Tkinter import *

'''root = Tk()
root.title("Menu dla zbiorow")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nowy", command=None)
filemenu.add_command(label="Otworz", command=None)
filemenu.add_command(label="Zapisz", command=None)
filemenu.add_command(label="Zapisz jako", command=None)
filemenu.add_command(label="Wyjscie", command=None)

filemenu.add_separator()

filemenu.add_command(label=u"Wyj\015bcie", command = root.quit)
menubar.add_cascade(label="Zbior", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cofnij",command=None)

editmenu.add_separator()

editmenu.add_command(label="Wytnij", command=None)
editmenu.add_command(label="Kopiuj", command=None)
editmenu.add_command(label="Wklej", command=None)
editmenu.add_command(label=u"Usu\0144", command=None)
editmenu.add_command(label="Wybierz wszystko", command=None)

menubar.add_cascade(label="Edycja", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Indeks Pomocy", command=None)
helpmenu.add_command(label="0...", command=None)
menubar.add_cascade(label="Pomoc", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()'''

# ---------------------------------------------------------------------
# canvas

'''root = Tk()
root.title("Przyklad Canvas")

canvas = Canvas(root, width=400, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(100, 100, 200, 200)
canvas.create_line(100, 200, 200, 300)
for i in range(1, 20, 2):
    canvas.create_line(i, 0, i, 50)
canvas.create_oval(10, 10, 300, 300, width=2, fill='yellow')
canvas.create_arc(100, 200, 300, 100, fill='green')
canvas.create_rectangle(50, 200, 300, 300, width=5,fill='#8f8fff')
canvas.create_line(600, 300, 150, 150, width=10,fill='red')
#photo = PhotoImage(file='x.jpg')
#canvas.create_image(50, 300, image=photo, anchor=NW)
widget = Label(canvas, text="Kolo", fg='white', bg='white')
widget.pack()
canvas.create_window(100, 100, window=widget)
canvas.create_text(100, 280, text='Prostokat')
root.mainloop()
'''

# ------------------------------------------------------------------
# choinka

root = Tk()
root.title("Choinka")
canvas = Canvas(root, width=500, height=800, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_polygon(100, 300, 250, 100, 400, 300, fill="green")
canvas.create_polygon(50, 450, 250, 200, 450, 450, fill="green")
canvas.create_polygon(0, 600, 250, 300, 500, 600, fill="green")
canvas.create_rectangle(230, 600, 290, 650, fill='brown')

canvas.create_oval(200, 200, 230, 230, fill='red')
canvas.create_oval(270, 210, 300, 240, fill='red')
canvas.create_oval(310, 320, 340, 350, fill='red')
canvas.create_oval(200, 320, 230, 350, fill='red')
canvas.create_oval(220, 380, 250, 410, fill='red')
canvas.create_oval(120, 370, 150, 400, fill='red')
canvas.create_oval(350, 370, 380, 400, fill='red')
canvas.create_oval(100, 500, 130, 530, fill='red')
canvas.create_oval(200, 510, 230, 540, fill='red')
canvas.create_oval(300, 490, 330, 520, fill='red')

canvas.create_polygon(210,80,240,80,250,50,260,80,290,80,265,100,275,130,250,110,225,130,235,100, fill='#D9D926')

root.mainloop()
