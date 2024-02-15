from tkinter import *
from random import randint

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Метереологічні дослідження")
        self.master.geometry("400x250")

        # Створення полотна
        self.canvas = Canvas(master, width=290, height=250)
        self.canvas.place(x=110, y=0)

        # Створення елементів керування
        self.Lbl_temperature = Label(master, text="Температура")
        self.Lbl_temperature.place(x=10, y=10)

        self.Lbox = Listbox(master)
        self.Lbox.place(x=10, y=40)

        self.Btn_build = Button(master, text="Побудувати", command=self.generate_temperatures)
        self.Btn_build.place(x=10, y=210)

    def generate_temperatures(self):
        # Очистка Listbox перед додаванням нових значень
        self.Lbox.delete(0, END)

        # Генеруємо 7 нових випадкових чисел
        temperatures = [randint(15, 25) for _ in range(7)]

        # Додавання згенерованих значень до Listbox
        for temp in temperatures:
            self.Lbox.insert(END, temp)

# Створення головного вікна
root = Tk()
app = TemperatureApp(root)
root.mainloop()