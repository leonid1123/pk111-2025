#06/05 и 13/05 контрольные работы

from tkinter import *
import pymysql


class App:
    def __init__(self):
        self.cnx = pymysql.connect(host="localhost",
                                   user="pk111",
                                   password="1234",
                                   database="pk111")
        self.cur = self.cnx.cursor()
        win = Tk()
        win.title("Повторение")
        win.geometry("350x300")
        title_lbl = Label(text="Процессоры")
        name_lbl = Label(text="Название")
        man_lbl = Label(text="Производитель")
        fr_lbl = Label(text="Частота")
        sok_lbl = Label(text="Сокет")
        self.name_entry = Entry()
        self.man_entry = Entry()
        self.fr_entry = Entry()
        self.sok_entry = Entry()
        add_btn = Button(text="Добавить", height=6, command=self.get_db_info)
        self.my_list = []
        self.my_list_var = Variable(value=self.my_list)
        my_view = Listbox(listvariable=self.my_list_var, width=55)
        style={"padx":5,"pady":5, "sticky":"W"}
        my_view.grid(row=0, column=0, columnspan=3, **style)
        name_lbl.grid(row=1, column=0, **style)
        man_lbl.grid(row=2, column=0, **style)
        fr_lbl.grid(row=3, column=0, **style)
        sok_lbl.grid(row=4, column=0, **style)
        self.name_entry.grid(row=1, column=1, **style)
        self.man_entry.grid(row=2, column=1, **style)
        self.fr_entry.grid(row=3, column=1, **style)
        self.sok_entry.grid(row=4, column=1, **style)
        add_btn.grid(row=1, column=2, rowspan=4, **style)
        win.mainloop()

    def add_item(self):
        name = self.name_entry.get()
        man = self.man_entry.get()
        fr = self.fr_entry.get()
        sok = self.sok_entry.get()
        if name and man and fr and sok:
            tmp_str = f"Название:{name}, производитель:{man}, частота:{fr}"
            self.my_list.append(tmp_str)
            self.my_list_var.set(self.my_list)

    def get_db_info(self):
        self.cur.execute("SELECT * FROM proc")
        ans = self.cur.fetchall()
        print(ans)
        for item in ans:
            print(item)
            print(f"name:{item[1]},manuf:{item[2]},freq:{item[3]}")







app = App()

