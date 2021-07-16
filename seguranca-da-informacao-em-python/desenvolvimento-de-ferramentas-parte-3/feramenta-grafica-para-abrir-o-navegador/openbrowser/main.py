import webbrowser

from tkinter import *

root = Tk()

root.title("Abrir browser")
root.geometry("300x200")

def google():
    webbrowser.open("https://www.google.com")


my_google = Button(root, text="Abrir o Google", command=google).pack(pady=20)
root.mainloop()
