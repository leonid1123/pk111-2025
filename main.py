from tkinter import *
import pymysql.cursors


class App:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x300")
        self.win.title("Мессенджер")
        self.messages = []
        self.messages_var = Variable(value=self.messages)
        self.msg_view = Listbox(width=45, listvariable=self.messages_var)
        self.msg_entry = Entry(width=30)
        self.send_btn = Button(text="Отправить", command=self.send_message)
        self.get_btn = Button(text="Получить", command=self.get_messages)

        self.win.columnconfigure(0, weight=5)
        self.win.columnconfigure(1, weight=1)
        self.msg_view.grid(row=0, column=0, columnspan=2, sticky=EW)
        self.msg_entry.grid(row=1, column=0, sticky=EW)
        self.send_btn.grid(row=1, column=1)
        self.get_btn.grid(row=2, column=0, columnspan=2, sticky=EW)

        self.cnx = pymysql.connect(
            host="192.168.1.61",
            user="messenger",
            password="1234",
            database="messenger"
        )
        self.cur = self.cnx.cursor()
        self.get_messages()
        self.update_messages()
        self.win.mainloop()

    def send_message(self):
        msg = self.msg_entry.get()
        if msg:
            sql = "INSERT INTO msg(message) VALUES (%s)"
            params = (msg,)
            self.cur.execute(sql, params)
            self.cnx.commit()
            self.msg_entry.delete(0, END)
            self.get_messages()

    def get_messages(self):
        self.cur.execute("SELECT message FROM msg")
        ans = self.cur.fetchall()
        new_messages = [item[0] for item in ans]
        if new_messages != self.messages:
            self.messages = new_messages
            self.messages_var.set(self.messages)
            self.msg_view.yview_moveto(1)

    def update_messages(self):
        self.get_messages()
        self.win.after(5000, self.update_messages)


app = App()
