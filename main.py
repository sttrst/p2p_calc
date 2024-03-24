from tkinter import *
from tkinter import ttk


def check_is_alpha(z):
    al = '0123456789.,'
    return all(x in al for x in z)


def on_click_count(c1, c2, p1, p2, ob):
    c1 = c1.get()
    c2 = c2.get()
    p1 = p1.get()
    p2 = p2.get()
    ob = ob.get()

    f1 = True

    if any(check_is_alpha(x) == False for x in [c1, p1]):
        cntg1_lbl.config(text='ОШИБКА')
        f1 = False
    else:
        ck1 = round(float(c1) * ((100 + float(p1)) / 100), 2)
        cntg1_lbl.config(text=f'{ck1}')

    if any(check_is_alpha(x) == False for x in [c2, p2]):
        cntg2_lbl.config(text='ОШИБКА')
        f1 = False
    else:
        ck2 = round(float(c2) * ((100 - float(p2)) / 100), 2)
        cntg2_lbl.config(text=f'{ck2}')

    if f1:
        sprd = round(((ck2 / ck1) - 1) * 100, 2)
        sprd_lbl.config(text=f'{sprd}')

    if check_is_alpha(ob) == False:
        prft_lbl.config(text='ОШИБКА')
    else:
        prft = round(sprd / 100 * float(ob), 2)
        prft_lbl.config(text=f'{prft}')


root = Tk()
root.title("p2p calc")
root.geometry("350x250")
root.iconbitmap(default="favicon.ico")
root.resizable(False, False)

cena1 = StringVar()
cena2 = StringVar()
prst1 = StringVar()
prst2 = StringVar()
oborot = StringVar()

for c in range(3):
    root.columnconfigure(index=c, weight=1)
for r in range(3):
    root.rowconfigure(index=r)

Label(root, text="    ").grid(row=0, column=0, ipadx=15, ipady=0, padx=5, pady=0)
Label(root, text="покупка").grid(row=0, column=1, ipadx=6, ipady=0, padx=5, pady=0)
Label(root, text="продажа").grid(row=0, column=2, ipadx=6, ipady=0, padx=5, pady=0)

Label(root, text="цена").grid(row=1, column=0, ipadx=15, ipady=6, padx=5, pady=0)
cena_entry_1 = ttk.Entry(root, textvariable=cena1)
cena_entry_1.insert(0, '0.0')
cena_entry_1.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=0)
cena_entry_2 = ttk.Entry(root, textvariable=cena2)
cena_entry_2.insert(0, '0.0')
cena_entry_2.grid(row=1, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="комиссия").grid(row=2, column=0, ipadx=15, ipady=6, padx=5, pady=0)
prst_entry_1 = ttk.Entry(root, textvariable=prst1)
prst_entry_1.insert(0, '0.0')
prst_entry_1.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=0)
prst_entry_2 = ttk.Entry(root, textvariable=prst2)
prst_entry_2.insert(0, '0.0')
prst_entry_2.grid(row=2, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="    ").grid(row=3, column=0, ipadx=15, ipady=6, padx=5, pady=0)
cntg1_lbl = Label(root, text="цена итого")
cntg2_lbl = Label(root, text="цена итого")
cntg1_lbl.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=0)
cntg2_lbl.grid(row=3, column=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="спред").grid(row=4, column=0, ipadx=15, ipady=6, padx=5, pady=0)
sprd_lbl = Label(root, text="сумма %")
sprd_lbl.grid(row=4, column=1, columnspan=2, ipadx=6, ipady=6, padx=5, pady=0)

Label(root, text="оборот").grid(row=5, column=0, ipadx=15, ipady=6, padx=5, pady=0)
oborot_entry = ttk.Entry(root, textvariable=oborot)
oborot_entry.insert(0, '0')
oborot_entry.grid(row=5, column=1, columnspan=2, ipadx=6, ipady=6, padx=6, pady=0)

ttk.Button(text="подсчёт", command=lambda: on_click_count(cena1, cena2, prst1, prst2, oborot)).grid(row=6, column=0,
                                                                                                    ipadx=6,
                                                                                                    ipady=6, padx=5,
                                                                                                    pady=5)
Label(root, text="прибыль").grid(row=6, column=1, ipadx=15, ipady=6, padx=5, pady=0)
prft_lbl = Label(root, text="сумма $")
prft_lbl.grid(row=6, column=2, ipadx=6, ipady=6, padx=6, pady=0)

root.mainloop()
