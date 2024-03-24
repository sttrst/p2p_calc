from tkinter import *
from tkinter import ttk

root = Tk()
root.title("p2p calc")
root.geometry("300x250")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)

for c in range(3):
    root.columnconfigure(index=c, weight=1)
for r in range(3):
    root.rowconfigure(index=r)

Label(root, text="    ").grid(row=0, column=0, ipadx=15, ipady=0, padx=5, pady=0)
Label(root, text="покупка").grid(row=0, column=1, ipadx=6, ipady=0, padx=5, pady=0)
Label(root, text="продажа").grid(row=0, column=2, ipadx=6, ipady=0, padx=5, pady=0)

Label(root, text="цена").grid(row=1, column=0, ipadx=15, ipady=6, padx=5, pady=0)
ttk.Entry().grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=0)
ttk.Entry().grid(row=1, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="комиссия").grid(row=2, column=0, ipadx=15, ipady=6, padx=5, pady=0)
ttk.Entry().grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=0)
ttk.Entry().grid(row=2, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="    ").grid(row=3, column=0, ipadx=15, ipady=6, padx=5, pady=0)
Label(root, text="цена итого").grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=0)
Label(root, text="цена итого").grid(row=3, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="спред").grid(row=4, column=0, ipadx=15, ipady=6, padx=5, pady=0)
Label(root, text="сумма %").grid(row=4, column=1, columnspan=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="оборот").grid(row=5, column=0, ipadx=15, ipady=6, padx=5, pady=0)
ttk.Entry().grid(row=5, column=1, columnspan=2, ipadx=6, ipady=6, padx=6, pady=0)

Label(root, text="прибыль").grid(row=6, column=0, ipadx=15, ipady=6, padx=5, pady=0)
ttk.Button(text="подсчёт").grid(row=6, column=1, ipadx=6, ipady=6, padx=5, pady=5)
Label(root, text="сумма $").grid(row=6, column=2, ipadx=6, ipady=6, padx=6, pady=0)

root.mainloop()
