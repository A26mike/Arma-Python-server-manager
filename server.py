from classes.basic_cfg import BasicCFG
from tkinter import filedialog
from tkinter import ttk
from tkinter import *


def getdir():
    window1.filename = filedialog.askopenfilename(initialdir="/", title="Get Directory",
                                                  filetypes=(("Arma Cfg", "*.cfg"), ("all files", "*.*")))

    print(window1.filename)



root = Tk()
window1 = root
#style css
style = ttk.Style()
current_theme = style.theme_use()
style.theme_settings(current_theme, {"TNotebook.Tab": {"configure": {"padding": [40, 0]}}})

root.title("Arma Server Manager")

tab_control = ttk.Notebook(root)
# create Tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

test = Button(tab1, text='Director', command=getdir)
test.grid(row=10, column=10)


def placeholder():
    pass


tab_control.add(tab1, text='Start up\n Parameters')
tab_control.add(tab2, text='Server\nConfig')
tab_control.add(tab3, text='Basic\nConfig')
tab_control.add(tab4, text='Network\n Monitor')

# create layout for tab 1
# TODO tab 1 (Start up/n Parameters)

tab1_cb1 = Checkbutton(tab1, text='AutoInit', command=placeholder)
tab1_cb2 = Checkbutton(tab1, text="bandwidthAlg=2", command=placeholder)

tab1_lb1 = Label(tab1, text='Game Port')
tab1_lb2 = Label(tab1, text='PID File name')
tab1_lb3 = Label(tab1, text='Ranking')
tab1_lb4 = Label(tab1, text='Netlog')
tab1_lb5 = Label(tab1, text='Basic cfg')
tab1_lb6 = Label(tab1, text='Server Config')

tab1_ent1 = Entry(tab1)
tab1_ent1.insert(0, "2302")
tab1_ent2 = Entry(tab1)
tab1_ent3 = Entry(tab1)
tab1_ent4 = Entry(tab1)
tab1_ent5 = Entry(tab1)
tab1_ent5.insert(0, "basic.cfg")
tab1_ent6 = Entry(tab1)
tab1_ent6.insert(0, "server.cfg")

tab1_cb1.grid(column=0, row=0)
tab1_cb2.grid(column=1, row=0, sticky=W)

tab1_lb1.grid(column=0, row=3, pady=10)
tab1_lb2.grid(column=0, row=4, pady=10)
tab1_lb3.grid(column=0, row=5, pady=10)
tab1_lb4.grid(column=0, row=6, pady=10)
tab1_lb5.grid(column=0, row=7, pady=10)
tab1_lb6.grid(column=0, row=8, pady=10)

tab1_ent1.grid(column=1, row=3, pady=10)
tab1_ent2.grid(column=1, row=4, pady=10)
tab1_ent3.grid(column=1, row=5, pady=10)
tab1_ent4.grid(column=1, row=6, pady=10)
tab1_ent5.grid(column=1, row=7, pady=10)
tab1_ent6.grid(column=1, row=8, pady=10)

# TODO fix Basic CFG generator


tab3_lb1 = Label(tab3, text='MTU')
tab3_lb2 = Label(tab3, text='Upload Speed in Mbps')
tab3_lb3 = Label(tab3, text='Intial Bandwitdth')
tab3_lb4 = Label(tab3, text='Slowest Players Download in Mbps')

tab3_ent1 = Entry(tab3)
tab3_ent2 = Entry(tab3)
tab3_ent3 = Entry(tab3)
tab3_ent4 = Entry(tab3)

tab3_lb1.grid(column=0, row=3, pady=10)
tab3_lb2.grid(column=0, row=4, pady=10)
tab3_lb3.grid(column=0, row=5, pady=10)
tab3_lb4.grid(column=0, row=6, pady=10)

tab3_ent1.grid(column=1, row=3, pady=10)
tab3_ent1.insert(0, "1400")
tab3_ent2.grid(column=1, row=4, pady=10)
tab3_ent2.insert(0, "25")
tab3_ent3.grid(column=1, row=5, pady=10)
tab3_ent3.insert(0, "5")
tab3_ent4.grid(column=1, row=6, pady=10)
tab3_ent4.insert(0, "1")

tab_control.pack(expand=1, fill='both')

window1.mainloop()
root.mainloop()


server_1 = BasicCFG(200, 5, 1
                    # (input("What is the server's Max Upload speed in megabit/s: \n ")),
                    # (input("Server initial bandwidth recommended 10-25mbit\n")),
                    # input("What is the slowest clients download speed in megabit/s:\n "))
                    )
server_1.print_arma_cfg()
