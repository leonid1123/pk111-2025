from tkinter import *
import pymysql


class App:
    def __init__(self):
        my_style = {'font':('Helvetica', 18)}
        paddings = { 'padx': 5, 'pady': 5}
        self.win = Tk()
        self.win.geometry("600x200")
        self.win.title("Авторизация")
        login_text = Label(text="Логин", **my_style)
        pass_text = Label(text="Пароль", **my_style)
        self.login_entry = Entry(**my_style)
        self.pass_entry = Entry(**my_style)
        btn = Button(text="Вход", **my_style, command=self.check_password)
        login_text.grid(row=0, column=0, **paddings)
        pass_text.grid(row=1, column=0, **paddings)
        self.login_entry.grid(row=0, column=1, **paddings)
        self.pass_entry.grid(row=1, column=1, **paddings)
        btn.grid(row=3, column=0, columnspan=2, **paddings)
        self.db_connect()
        self.win.mainloop()

    def db_connect(self):
        self.cnx = pymysql.connect(host="localhost",
                                   user="pk111",
                                   password="1234",
                                   database="users")
        self.cur = self.cnx.cursor()

    def check_password(self):
        login = self.login_entry.get()
        password = self.pass_entry.get()
        sql = """SELECT password 
                FROM user
                 WHERE login = %s"""
        params = (login,)
        self.cur.execute(sql,params)
        ans = self.cur.fetchall()
        tmp = ans[0]
        db_pass = tmp[0]
        print(db_pass)



app = App()
