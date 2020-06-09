from classes.basic_cfg import BasicCFG
from tkinter import *

from tkinter import ttk



window = Tk()

window.title("Arma Server Manager")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)


tab_control.add(tab1, text='Start up Perams')
tab_control.add(tab2, text='server.cfg')
tab_control.add(tab3, text='Basic.cfg')
var1 = IntVar()
cb1 = Checkbutton(tab1, text="-autoInit", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
cb2 = Checkbutton(tab1, text="-bandwidthAlg=2", variable=var2).grid(row=1, sticky=W)

lbl1 = Label(tab1, text= 'label1')
lbl2 = Label(tab2, text= 'label2')

lbl1.grid(column=2, row=0)


tab_control.pack(expand=1, fill='both')

window.mainloop()


server_1 =BasicCFG( 200,5,1
    # (input("What is the server's Max Upload speed in megabit/s: \n ")),
    # (input("Server initial bandwidth recommended 10-25mbit\n")),
    # (input("What is the slowest clients download speed in megabit/s:\n "))
)
server_1.print_arma_cfg()