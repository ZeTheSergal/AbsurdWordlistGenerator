import itertools
from tkinter import *





def Make():
    min_length = int(MIN.get())
    max_length = int(MAX.get())
    chrs = ''
    Total = 0
    Size = 0
    if (bool(CAP.get())):
        chrs = chrs + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Total = Total + 26
    if (bool(small.get())):
        chrs = chrs + "abcdefghijklmnopqrstuvwxyz"
        Total = Total + 26
    if (bool(Num.get())):
        chrs = chrs + "0123456789"
        Total = Total + 10
    if (bool(Sym.get())):
        chrs = chrs + "\|¬¦!\"£$%^&*()-_=+[{]};:@'~#<,>.?/áéúíó"
        Total = Total + 40

    for Loop in range (max_length):
        Size = Size + ((Total ** (Loop + 1)) * (Loop + 2))
            
    Con = Toplevel(master)
    X = Button(Con, text="File Size Will Be: " + str(Size * 0.000000001) + "Gb or " + str(Size) + " Bytes. Confirm?", command=Make2)
    X.pack()




def Make2():
    min_length = int(MIN.get())
    max_length = int(MAX.get())
    chrs = ''
    Total = 0
    Size = 0
    if (bool(CAP.get())):
        chrs = chrs + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Total = Total + 26
    if (bool(small.get())):
        chrs = chrs + "abcdefghijklmnopqrstuvwxyz"
        Total = Total + 26
    if (bool(Num.get())):
        chrs = chrs + "0123456789"
        Total = Total + 10
    if (bool(Sym.get())):
        chrs = chrs + "\|¬¦!\"£$%^&*()-_=+[{]};:@'~#<,>.?/áéúíó"
        Total = Total + 40
    file = open((Name.get()),"w")
    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            file.write((''.join(xs)) + "\n")

    file.close()
    newwin = Toplevel(master)
    display = Label(newwin, text="Done!")
    display.pack()  


master = Tk()

CAP = IntVar() 
small = IntVar()
Num = IntVar() 
Sym = IntVar()

Label(master, text="Min Length").grid(row=0,column=0)
Label(master, text="Max Length").grid(row=1)
Label(master, text="Charcater Sets").grid(row=2)
Label(master, text="File Name").grid(row=3)

MIN = Entry(master)
MIN.grid(row=0,column=1)
MAX = Entry(master)
MAX.grid(row=1,column=1)
Name = Entry(master)
Name.grid(row=3,column=1)

CAP1 = Checkbutton(master, text="<A-Z>", variable=CAP)
CAP1.grid(row=2,column=1)
small1 = Checkbutton(master, text="<a-z>", variable=small)
small1.grid(row=2,column=2)
Num1 = Checkbutton(master, text="<0-9>", variable=Num)
Num1.grid(row=2,column=3)
Sym1 = Checkbutton(master, text="<Symbols>", variable=Sym)
Sym1.grid(row=2,column=4)


Button(master, text='Genarate', command=Make).grid(row=4, column=0, sticky=W, pady=4)

mainloop( )

