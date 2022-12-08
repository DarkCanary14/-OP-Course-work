import Enter
import sqlite3
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import re
from tkinter.messagebox import showerror


class MainForm:

    def __init__(self, usr):

        self.user_id = usr[1]
        # Prepare for decrypt and encrypt
        self.alpha = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # self.text = ''
        self.key = [[15, 4], [11, 3]]
        self.reverse_key = [[3, -4], [-11, 15]]

        main_win = tk.Tk()
        main_win.title('Hill Cipher')
        main_win.geometry('966x520')

        label_cent = tk.Label(text='Hello!\nThere you can encrypt or decrypt your message.')
        label_cent.grid(row=0, column=1)

        center_btn = tk.Button(text='Check\nhistory', command=self.out_all)
        center_btn.grid(row=3, column=1)

        # Graphical elements of encryption
        label1 = tk.Label(text='Encryption')
        label1.grid(row=1, column=0)
        self.text_box1 = tk.scrolledtext.ScrolledText(wrap='word', font=('Verdana', 13), width=30, height=10)
        self.text_box1.grid(row=2, column=0)
        btn1 = tk.Button(text='Encrypt', command=self.encrypt)
        btn1.grid(row=3, column=0)
        label2 = tk.Label(text='Result')
        label2.grid(row=4, column=0)
        self.text_box2 = tk.scrolledtext.ScrolledText(wrap='word', font=('Verdana', 13), width=30, height=10)
        self.text_box2.grid(row=5, column=0)

        # Graphical elements of decryption
        label1 = tk.Label(text='Decryption')
        label1.grid(row=1, column=2)
        self.text_box3 = tk.scrolledtext.ScrolledText(wrap='word', font=('Verdana', 13), width=30, height=10)
        self.text_box3.grid(row=2, column=2)
        btn2 = tk.Button(text='Decrypt', command=self.decrypt)
        btn2.grid(row=3, column=2)
        label1 = tk.Label(text='Result')
        label1.grid(row=4, column=2)
        self.text_box4 = tk.scrolledtext.ScrolledText(wrap='word', font=('Verdana', 13), width=30, height=10)
        self.text_box4.grid(row=5, column=2)

        main_win.mainloop()

    def out_all(self):
        conn = sqlite3.connect('encryption.db')
        cur = conn.cursor()

        # cur.execute('drop table notes')

        cur.execute('''create table if not exists notes(
                                    note_id integer primary key autoincrement,
                                    message text not null,
                                    encrypt_mess text not null,
                                    user_id references users(userid) on update cascade)''')

        cur.execute('select message, encrypt_mess from notes where user_id = ?', (self.user_id[0],))
        result = cur.fetchall()
        conn.commit()

        history_win = tk.Tk()
        history_win.title('Hill Cipher')
        history_win.geometry('300x150')

        content = tk.Text(history_win)
        content.pack(fill=tk.BOTH, expand=1)

        for i in result:
            content.insert(tk.END, i)
            content.insert(tk.END, '\n')
        history_win.mainloop()

    @staticmethod
    def prepare_text(text, alphabet):
        if (text == '') or text.isspace():
            return None

        messg = text.upper()
        messg = re.sub('\n', '', messg)
        messg = re.sub(' ', '', messg)
        messg = re.sub(r'[^\w\s]', '', messg)

        if (messg == '') or messg.isspace():
            return None

        for letter in messg:
            if letter not in alphabet:
                return None

        if (len(messg)) % 2 != 0:
            messg += 'Z'

        template = r'[A-Z]{2}'  # Regular expression
        message = re.findall(template, messg)

        return message

    def encrypt_decrypt(self, message, matrix):
        if message is None or message == '':
            showerror(title='Error', message='This text is incorrect')
            return None

        sum_all = 0
        output = ''
        for i in range(len(message)):
            for string in range(2):
                for column in range(2):
                    sum_all += matrix[string][column] * self.alpha.index(message[i][column])  # [i][column]
                output += self.alpha[sum_all % 26]
                sum_all = 0
        return output

    def encrypt(self):
        text = self.text_box1.get('1.0', tk.END)
        text = self.prepare_text(text, self.alpha)
        message = self.encrypt_decrypt(text, self.key)
        if message is None:
            message = ''
        self.text_box2.delete('1.0', tk.END)
        self.text_box2.insert(tk.END, message)

        # Save in base
        text_for_base = self.text_box1.get('1.0', tk.END)
        text_for_base = re.sub('\n', '', text_for_base)

        conn = sqlite3.connect('encryption.db')
        cur = conn.cursor()
        cur.execute('''create table if not exists notes(
                            note_id integer primary key autoincrement,
                            message text not null,
                            encrypt_mess text not null,
                            user_id integer references users(userid) on update cascade)''')

        cur.execute('insert into notes(message, encrypt_mess, user_id) values (?, ?, ?)',
                    (text_for_base, message, self.user_id[0]))

        conn.commit()

    def decrypt(self):
        text = self.text_box3.get('1.0', tk.END)
        text = self.prepare_text(text, self.alpha)
        message = self.encrypt_decrypt(text, self.reverse_key)
        if message is None:
            message = ''
        self.text_box4.delete('1.0', tk.END)
        self.text_box4.insert(tk.END, message)


# MAIN PROGRAM
enter = [False, 0]
login = Enter.EntryForm(enter)

if enter[0] is True:
    win1 = MainForm(enter)
