from tkinter import *
import pymysql


class App:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x200")
        self.win.title("Авторизация")
        login_text = Label(text="Логин")
        pass_text = Label(text="Пароль")
        login_entry = Entry()
        pass_entry = Entry()
        btn = Button(text="Вход")
        login_text.grid(row=0, column=0)
        pass_text.grid(row=1, column=0)
        login_entry.grid(row=0, column=1)
        pass_entry.grid(row=1, column=1)
        btn.grid(row=3, column=0, columnspan=2)
        self.db_connect()
        self.win.mainloop()

    def db_connect(self):
        self.cnx = pymysql.connect(host="localhost",
                                   user="pk111",
                                   password="1234",
                                   database="users")
        self.cur = self.cnx.cursor()

app = App()
