from tkinter import *
import pymysql


class App:
    def __init__(self):
        my_style = {'font': ('Helvetica', 18)}
        paddings = {'padx': 5, 'pady': 5}
        self.reg_win = None
        self.win = Tk()
        self.win.geometry("600x200")
        self.win.title("Авторизация")
        login_text = Label(text="Логин", **my_style)
        pass_text = Label(text="Пароль", **my_style)
        self.login_entry = Entry(**my_style)
        self.pass_entry = Entry(**my_style)
        btn = Button(text="Вход", **my_style, command=self.check_password)
        reg_btn = Button(text="Регистрация",
                         **my_style,
                         command=self.register_user)
        login_text.grid(row=0, column=0, **paddings)
        pass_text.grid(row=1, column=0, **paddings)
        self.login_entry.grid(row=0, column=1, **paddings)
        self.pass_entry.grid(row=1, column=1, **paddings)
        btn.grid(row=2, column=0, **paddings)
        reg_btn.grid(row=2, column=1, **paddings)
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
        self.cur.execute(sql, params)
        ans = self.cur.fetchall()
        tmp = ans[0]
        db_pass = tmp[0]
        print(db_pass)
        if db_pass == password:
            print("ok")
        else:
            print("не ok")

    def register_user(self):
        if self.reg_win is None:
            self.reg_win = Tk()
            self.reg_win.title("Регистрация")
            self.reg_win.geometry("500x300")
            lbl_names = ["Логин", "Пароль", "Повторите пароль"]
            for row, item in enumerate(lbl_names, start=0):
                Label(self.reg_win, text=item).grid(row=row, column=0)
            self.new_login_entry = Entry(self.reg_win)
            self.new_pass_entry1 = Entry(self.reg_win)
            self.new_pass_entry2 = Entry(self.reg_win)
            self.new_login_entry.grid(row=0, column=1)
            self.new_pass_entry1.grid(row=1, column=1)
            self.new_pass_entry2.grid(row=2, column=1)
            Button(self.reg_win, text="Регистрация",
                   command=self.reg_user).grid(row=3,
                                               column=0,
                                               columnspan=2)
            self.reg_win.mainloop()

    def reg_user(self):
        new_login = self.new_login_entry.get()
        new_pass1 = self.new_pass_entry1.get()
        new_pass2 = self.new_pass_entry2.get()
        if new_pass1 == new_pass2:
            sql = """SELECT id FROM users
            WHERE login=%s"""
            params = (new_login,)
            self.cur.execute(sql,params)
            ans = self.cur.fetchone()
            if ans:
                print("такое имя занято")
        else:
            print("Пароли не совпадают!")


app = App()
