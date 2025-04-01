from tkinter import *


class Fruits:
    def __init__(self, _name, _fresh, _weight):
        self.name = _name
        self.fresh = _fresh
        self.weight = _weight

    def __str__(self):
        return f"Название:{self.name},свежесть:{self.fresh},вес:{self.weight}"


class App:
    def __init__(self):
        self.fruit_list = []
        self.win = Tk()
        self.win.title("Склад")
        self.win.geometry("600x400")
        self.fruit_name_label = Label(text="Название:")
        self.fruit_fresh_label = Label(text="Свежесть:")
        self.fruit_weight_label = Label(text="Вес:")
        self.name_entry = Entry()
        self.fresh_entry = Entry()
        self.weight_entry = Entry()
        self.btn = Button(text="Добавить")
        self.btn.bind('<Button>', self.add_fruit, add=None)

        self.fruit_var = Variable(value=self.fruit_list)
        self.fruit_view = Listbox(listvariable=self.fruit_var, width=50)
        self.fruit_view.grid(row=0, column=2, rowspan=5)

        self.fruit_name_label.grid(row=0, column=0)
        self.fruit_fresh_label.grid(row=1, column=0)
        self.fruit_weight_label.grid(row=2, column=0)
        self.name_entry.grid(row=0,column=1)
        self.fresh_entry.grid(row=1, column=1)
        self.weight_entry.grid(row=2, column=1)
        self.btn.grid(row=4, column=0, columnspan=2)

        self.win.mainloop()

    def add_fruit(self, event):
        fruit = Fruits(self.name_entry.get(),
                       self.fresh_entry.get(),
                       self.weight_entry.get())
        self.fruit_list.append(fruit)
        self.fruit_var.set(self.fruit_list)

        print(self.name_entry.get())
        print(self.fresh_entry.get())
        print(self.weight_entry.get())


myApp = App()

"""
Склад мобильных телефонов.
класс с 4 параметрами.
сделать приложение для внесения позиций
на склад.
на оценку!
"""







