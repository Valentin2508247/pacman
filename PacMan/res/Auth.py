from tkinter import *
from tkinter import messagebox
from res.database import Database

import hashlib


class Authorization:
    def __init__(self):
        self.root = Tk()
        self.root.title("Authorization")
        self.root.geometry("600x600")
        self.root.configure(bg="black")

        log_in_btn = Button(text="Log in", background="#555", foreground="#ccc",
                            padx="20", pady="8", font="16", command=self.log_in)

        log_in_btn.place(relx=.605, rely=.6, anchor="c", height=30, width=130, bordermode=OUTSIDE)

        sign_in_btn = Button(text="Sign in", background="#555", foreground="#ccc",
                             padx="20", pady="8", font="16", command=self.sign_in)

        sign_in_btn.place(relx=.395, rely=.6, anchor="c", height=30, width=130, bordermode=OUTSIDE)

        self.login = StringVar()
        self.password = StringVar()

        entry_login = Entry(textvariable=self.login)
        entry_login.place(relx=.5, rely=.4, anchor="c", height=25, width=300)

        entry_password = Entry(textvariable=self.password, show='*')
        entry_password.place(relx=.5, rely=.5, anchor="c", height=25, width=300)

        self.root.protocol("WM_DELETE_WINDOW", lambda: exit())
        self.db = Database("database", "user_data")
        self.cur_db = None
        self.name = None
        self.root.mainloop()

    @staticmethod
    def hash_password(password):
        h = hashlib.sha512(password.encode('utf-8'))
        return h.hexdigest()

    def sign_in(self):
        if not self.password.get() and not self.login.get():
            messagebox.showinfo("Warning", "Empty data")
        elif not self.login.get():
            messagebox.showinfo("Warning", "Empty login")
        elif not self.password.get():
            messagebox.showinfo("Warning", "Empty password")
        elif len(self.password.get()) < 8:
            messagebox.showinfo("Warning", "Too short password")
        elif self.db.find_login(self.login.get()):
            messagebox.showinfo("Warning", "This user is already exists")
        else:
            self.db.add_user(self.login.get(), self.hash_password(self.password.get()))
            messagebox.showinfo("OK", "Done")

    def log_in(self):
        if not self.password.get() and not self.login.get():
            messagebox.showinfo("Warning", "Empty data")
        elif not self.login.get():
            messagebox.showinfo("Warning", "Empty login")
        elif not self.password.get():
            messagebox.showinfo("Warning", "Empty password")
        elif self.db.find_user(self.login.get(), self.hash_password(self.password.get())):
            self.name = self.login.get()
            self.cur_db = Database("database", "table_of_records")
            self.root.destroy()
        else:
            messagebox.showinfo("Warning", "Wrong data")

#Authorization()