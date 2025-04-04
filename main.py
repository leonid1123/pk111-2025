from tkinter import *
from datetime import datetime
from tkcalendar import DateEntry
"""
сделать ввод даты, проверку на текущую дату и изменение свежести
привязать всё к БД
"""


class Fruits:
    def __init__(self, _name, _fresh, _weight):
        self.name = _name
        self.fresh = _fresh
        self.weight = _weight

    def __str__(self):
        return f"Название:{self.name},свежесть:{self.fresh},вес:{self.weight}"


class App:
    def __init__(self):
        self.today = datetime.today().date()
        print(self.today)
        self.fruit_list = []
        self.win = Tk()
        self.win.title("Склад")
        self.win.geometry("600x400")
        self.fruit_name_label = Label(text="Название:")
        self.fruit_fresh_label = Label(text="Свежесть:")
        self.fruit_weight_label = Label(text="Вес:")
        self.fruit_date = Label(text="Дата поставки: ")
        self.name_entry = Entry()
        self.fresh_entry = Entry()
        self.weight_entry = Entry()
        self.btn = Button(text="Добавить")
        self.btn.bind('<Button>', self.add_fruit, add=None)
        self.date_picker = DateEntry(width=12, background='darkblue', foreground='white', borderwidth=2)

        self.fruit_var = Variable(value=self.fruit_list)
        self.fruit_view = Listbox(listvariable=self.fruit_var, width=50)
        self.fruit_view.grid(row=0, column=2, rowspan=5)

        self.fruit_name_label.grid(row=0, column=0)
        self.fruit_fresh_label.grid(row=1, column=0)
        self.fruit_weight_label.grid(row=2, column=0)
        self.fruit_date.grid(row=3, column=0)
        self.name_entry.grid(row=0,column=1)
        self.fresh_entry.grid(row=1, column=1)
        self.weight_entry.grid(row=2, column=1)
        self.date_picker.grid(row=3,column=1)
        self.btn.grid(row=4, column=0, columnspan=2)

        self.win.mainloop()

    def add_fruit(self, event):
        fruit = Fruits(self.name_entry.get(),
                       self.fresh_entry.get(),
                       self.weight_entry.get())
        self.fruit_list.append(fruit)
        self.fruit_var.set(self.fruit_list)

        print((self.date_picker.get_date()-self.today).days)

        print(self.name_entry.get())
        print(self.fresh_entry.get())
        print(self.weight_entry.get())


myApp = App()


"""
https://github.com/leonid1123/pk111-2025
Склад мобильных телефонов.
класс с 4 параметрами.
сделать приложение для внесения позиций
на склад.
на оценку!
"""







