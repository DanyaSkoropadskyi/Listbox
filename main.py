from tkinter import *
from random import randint

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Метереологічні дослідження")
        self.master.geometry("400x250")

        self.canvas = Canvas(self.master, width=290, height=250)
        self.canvas.place(x=110, y=0)

        self.Lbl_temperature = Label(self.master, text="Температура")
        self.Lbl_temperature.place(x=10, y=10)

        self.Lbox = Listbox(self.master)
        self.Lbox.place(x=10, y=40)

        self.Btn_build = Button(self.master, text="Побудувати", command=self.build_random_temperatures)
        self.Btn_build.place(x=10, y=210)

    def build_random_temperatures(self):

        self.Lbox.delete(0, END)

        for _ in range(7):
            temperature = randint(15, 25)
            self.Lbox.insert(END, temperature)

root = Tk()
app = TemperatureApp(root)

root.mainloop()