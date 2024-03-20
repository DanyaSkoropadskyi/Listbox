from tkinter import *

def calculate_frequencies():
    text = Txt.get("1.0", 'end-1c')
    Lbox1.delete(0, END)
    Lbox2.delete(0, END)
    total_chars = len(text)
    count_a = text.count('а')
    Lbox1.insert(END, count_a)
    if total_chars > 0:
        freq = count_a / total_chars
        Lbox2.insert(END, "{:.3f}".format(freq))

tk = Tk()
tk.title("Символьний калькулятор")
tk.geometry("440x280")

Lbl1 = Label(text="Введіть текст")
Lbl1.place(x=20, y=20)
Txt = Text(wrap=WORD)
Txt.place(x=20, y=50, width=120, height=160)
Btn = Button(text="Обчислити", command=calculate_frequencies)
Btn.place(x=160, y=20)
Lbox1 = Listbox()
Lbox1.place(x=160, y=50, width=120, height=160)
Lbl3 = Label(text="Частота входжень")
Lbl3.place(x=300, y=20)
Lbox2 = Listbox()
Lbox2.place(x=300, y=50, width=120, height=160)

tk.mainloop()
