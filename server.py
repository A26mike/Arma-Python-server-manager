from classes.basic_cfg import BasicCFG
from tkinter import *

from tkinter import ttk



window = Tk()
style = ttk.Style()                     
current_theme =style.theme_use()
style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [40, 0]}}})  

window.title("Arma Server Manager")

tab_control = ttk.Notebook(window)
#create Tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

def placeholer():
    pass

tab_control.add(tab1, text='Start up\n Parameters')
tab_control.add(tab2, text='Server\nConfig')
tab_control.add(tab3, text='Basic\nConfig')
tab_control.add(tab4, text='Network\n Monitor')

#create layout for tab 1 
#TODO tab 1 (Start up/n Parameters)
cb1 = Checkbutton(tab1, text='AutoInit', command=placeholer)
cb2 = Checkbutton(tab1, text="bandwidthAlg=2", command=placeholer)

lb1 = Label(tab1,text ='Port')
lb2 = Label(tab1,text ='PID File name')
lb3 = Label(tab1,text ='Ranking')
lb4 = Label(tab1,text ='Netlog')
lb5 = Label(tab1,text ='Basic cfg')
lb6 = Label(tab1,text ='Server Config')

ent1= Entry(tab1)
ent2= Entry(tab1)
ent3= Entry(tab1)
ent4= Entry(tab1)
ent5= Entry(tab1)
ent6= Entry(tab1)

cb1.grid(column=0, row=0)
cb2.grid(column=1, row=0, sticky=W)

lb1.grid(column=0, row=3, pady=10)
lb2.grid(column=0, row=4 , pady=10)
lb3.grid(column=0, row=5, pady=10)
lb4.grid(column=0, row=6, pady=10)
lb5.grid(column=0, row=7, pady=10)
lb6.grid(column=0, row=8, pady=10)

ent1.grid(column=1, row=3, pady=10)
ent2.grid(column=1, row=4, pady=10)
ent3.grid(column=1, row=5, pady=10)
ent4.grid(column=1, row=6, pady=10)
ent5.grid(column=1, row=7, pady=10)
ent6.grid(column=1, row=8, pady=10)

#TODO fix Basic CFG generator 


t3lb1 = Label(tab3,text ='Max Packet size')
t3lb2 = Label(tab3,text ='Upload Speed in Mb/s')
t3lb3 = Label(tab3,text ='Intial Bandwitdth')
t3lb4 = Label(tab3,text ='Slowest Players Download')


t3ent1= Entry(tab3)
t3ent2= Entry(tab3)
t3ent3= Entry(tab3)
t3ent4= Entry(tab3)



t3lb1.grid(column=0, row=3, pady=10)
t3lb2.grid(column=0, row=4 , pady=10)
t3lb3.grid(column=0, row=5, pady=10)
t3lb4.grid(column=0, row=6, pady=10)


t3ent1.grid(column=1, row=3, pady=10)
t3ent2.grid(column=1, row=4, pady=10)
t3ent3.grid(column=1, row=5, pady=10)
t3ent4.grid(column=1, row=6, pady=10)



tab_control.pack(expand=1, fill='both')

window.mainloop()


server_1 =BasicCFG( 200,5,1
    # (input("What is the server's Max Upload speed in megabit/s: \n ")),
    # (input("Server initial bandwidth recommended 10-25mbit\n")),
    # (input("What is the slowest clients download speed in megabit/s:\n "))
)
server_1.print_arma_cfg()