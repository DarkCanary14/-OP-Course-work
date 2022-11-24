import tkinter as tk
import sqlite3
import hashlib as hsh
from tkinter.messagebox import showerror, showinfo


class EntryForm:
    def __init__(self, enter):
        self.s = enter
        self.ent3 = None
        self.ent4 = None
        self.ent5 = None

        self.entry_win = tk.Tk()
        self.entry_win.title("Hill Cipher")
        self.entry_win.geometry('240x200')

        # empty labels
        label0 = tk.Label(self.entry_win, text='     ')
        label0.grid(row=0, column=0)
        label01 = tk.Label(self.entry_win, text='     ')
        label01.grid(row=4, column=0)

        label1 = tk.Label(self.entry_win, text='Login:')
        label1.grid(row=1, column=1)
        self.ent1 = tk.Entry(self.entry_win)
        self.ent1.grid(row=1, column=2)

        label2 = tk.Label(self.entry_win, text='Password:')
        label2.grid(row=2, column=1)
        self.ent2 = tk.Entry(self.entry_win, show='*')
        self.ent2.grid(row=2, column=2)

        btn1 = tk.Button(self.entry_win, text="log in", command=self.entry)
        btn1.grid(row=3, column=2)

        btn2 = tk.Button(self.entry_win, text="registration", command=self.registration)
        btn2.grid(row=5, column=2)

        self.entry_win.mainloop()

    def registration(self):

        reg_window = tk.Tk()
        reg_window.title('Hill Cipher')
        reg_window.geometry('270x200')

        # empty labels
        lbl0 = tk.Label(reg_window, text=' ')
        lbl0.grid(column=0, row=0)
        lbl01 = tk.Label(reg_window, text=' ')
        lbl01.grid(column=0, row=2)
        lbl02 = tk.Label(reg_window, text=' ')
        lbl02.grid(column=2, row=6)

        lbl_center = tk.Label(reg_window, text='Registration')
        lbl_center.grid(column=2, row=0)

        lbl1 = tk.Label(reg_window, text='Login')
        lbl1.grid(column=0, row=1)
        self.ent3 = tk.Entry(reg_window, width=30)  # login
        self.ent3.grid(column=2, row=1)

        lbl2 = tk.Label(reg_window, text='Password')
        lbl2.grid(column=0, row=3)
        self.ent4 = tk.Entry(reg_window, width=30, show='*')  # password
        self.ent4.grid(column=2, row=3)

        self.ent5 = tk.Entry(reg_window, width=30, show='*')  # password again
        self.ent5.grid(column=2, row=4)

        btn1 = tk.Button(reg_window, text='Register', command=self.reg)
        btn1.grid(column=2, row=5)

        btn2 = tk.Button(reg_window, text='Exit', command=reg_window.destroy)  # Exit button
        btn2.grid(column=2, row=7)

        reg_window.mainloop()

    def entry(self):
        log = self.ent1.get()
        pas = self.ent2.get()

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists users(
                    userid integer primary key autoincrement,
                    login text not null,
                    password text not null)''')

        cur.execute('select userid from users where login = ? and password = ?', (log, self.MD5(pas),))
        res = cur.fetchone()
        conn.commit()

        if res is None:
            showerror(title='Error', message='User not found')
        else:
            showinfo(title='Success', message='Welcome!')
            self.s[0] = True
            self.entry_win.destroy()

    def reg(self):
        log = self.ent3.get()
        pas = self.MD5(self.ent4.get())
        pas2 = self.MD5(self.ent5.get())
        if pas != pas2:
            showerror(title='Error', message="Passwords don't much")
            return

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists users(
                    userid integer primary key autoincrement,
                    login text not null,
                    password text nt null)''')

        cur.execute('select login from users where login = ?', (log,))
        res = cur.fetchone()
        conn.commit()

        if res is not None:
            showerror(title='Error', message='This login already exists')
            return

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('insert into users(login, password) values(?, ?)', (log, pas))
        conn.commit()

    @staticmethod
    def MD5(passwd=''):
        enc_pass = hsh.md5(passwd.encode('utf-8'))
        return enc_pass.hexdigest()
