from tkinter import *

root = Tk()

def apresentar1():
    print(valor_check_1.get())

def apresentar2():
    print(valor_check_2.get())

def apresentar3():
    print(valor_check_3.get())

def apresentar4():
    print(valor_check_4.get())

def apresentar5():
    print(valor_check_5.get())

def apresentar6():
    print(valor_check_6.get())

def apresentar7():
    print(valor_check_7.get())

def apresentar8():
    print(valor_check_8.get())

def apresentar9():
    print(valor_check_9.get())

def apresentar10():
    print(valor_check_10.get())

valor_check_1 = IntVar()
valor_check_2 = IntVar()
valor_check_3 = IntVar()
valor_check_4 = IntVar()
valor_check_5 = IntVar()
valor_check_6 = IntVar()
valor_check_7 = IntVar()
valor_check_8 = IntVar()
valor_check_9 = IntVar()
valor_check_10 = IntVar()


check = Checkbutton(root, text="Opção 1", variable=valor_check_1, command=apresentar1).pack()
check = Checkbutton(root, text="Opção 2", variable=valor_check_2, command=apresentar2).pack()
check = Checkbutton(root, text="Opção 3", variable=valor_check_3, command=apresentar3).pack()
check = Checkbutton(root, text="Opção 4", variable=valor_check_4, command=apresentar4).pack()
check = Checkbutton(root, text="Opção 5", variable=valor_check_5, command=apresentar5).pack()
check = Checkbutton(root, text="Opção 6", variable=valor_check_6, command=apresentar6).pack()
check = Checkbutton(root, text="Opção 7", variable=valor_check_7, command=apresentar7).pack()
check = Checkbutton(root, text="Opção 8", variable=valor_check_8, command=apresentar8).pack()
check = Checkbutton(root, text="Opção 9", variable=valor_check_9, command=apresentar9).pack()
check = Checkbutton(root, text="Opção 10", variable=valor_check_10, command=apresentar10).pack()

root.mainloop()