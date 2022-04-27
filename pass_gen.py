import tkinter as tk
from tkinter import ttk
import secrets
import string


def gen_pass():
    try:
        pw = ""
        chars = string.digits + string.ascii_letters + string.punctuation
        leange = int(laenge_entry.get())
        for _ in range(leange):
            pw = pw+secrets.choice(chars)
        pw_value.set(pw)
    except ValueError:
        pw_value.set('Bitte einen gültigen Zahlenwert eingeben')

root = tk.Tk()
root.geometry('750x250')
root.title('Passwortgenerator')

pw_value = tk.StringVar(value='Hier erscheint dein generiertes Passwort gleich...')

laenge = ttk.Label(root, text='Wähle die länge deines Passwortes aus:', font=('Arial', 18))
laenge.pack(side='top', fill='x', padx='5', pady='5')

laenge_entry = ttk.Entry(root, font=('Arial', 18))
laenge_entry.pack(side='top', fill='x', padx='5', pady='5')

passwd = ttk.Label(root, text='Dein Passwort:', font=('Arial', 18))
passwd.pack(side='top', fill='x', padx='5', pady='5')

pw_display = ttk.Entry(root, textvariable=pw_value, font=('Arial', 18))
pw_display.pack(side='top', fill='x', padx='5', pady='5')

gen_pw_button = ttk.Button(root, text='Passwort generieren', command=gen_pass)
gen_pw_button.pack(side='bottom', fill='x', padx='5', pady='5')

root.mainloop()
