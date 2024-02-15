from tkinter import *

# Створення головного вікна
tk = Tk()
tk.title("Метереологічні дослідження")
tk.geometry("400x250")

# Створення полотна
canvas = Canvas(tk, width=290, height=250)
canvas.place(x=110, y=0)

# Створення елементів керування
Lbl_temperature = Label(tk, text="Температура")
Lbl_temperature.place(x=10, y=10)

Lbox = Listbox(tk)
Lbox.place(x=10, y=40)

Btn_build = Button(tk, text="Побудувати")
Btn_build.place(x=10, y=210)

# Запуск головного циклу програми
tk.mainloop()