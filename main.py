import tkinter as tk
from random import randint

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Метеорологічні дослідження")
        self.master.geometry("400x250")

        self.canvas = tk.Canvas(master, width=290, height=250)
        self.canvas.place(x=110, y=0)  

        self.temperature_label = tk.Label(master, text="Температура")
        self.temperature_label.grid(row=0, column=0)

        self.temperature_listbox = tk.Listbox(master)
        self.temperature_listbox.grid(row=1, column=0)

        self.build_button = tk.Button(master, text="Побудувати", command=self.build_graph)
        self.build_button.grid(row=2, column=0)

    def generate_temperatures(self):
        return [randint(15, 25) for _ in range(7)]

    def build_graph(self):
        temperatures = self.generate_temperatures()
        self.temperature_listbox.delete(0, tk.END)
        for temp in temperatures:
            self.temperature_listbox.insert(tk.END, temp)

        x_increment = 290 / 7
        x = 0
        prev_x, prev_y = None, None
        for temp in temperatures:
            y = 250 - (temp - 15) * (250 / 10) 
            self.canvas.create_oval(x, y, x + 3, y + 3, fill="red" if temp == max(temperatures) else "green")
            if prev_x is not None and prev_y is not None:
                self.canvas.create_line(prev_x, prev_y, x, y, fill="blue")
            prev_x, prev_y = x, y
            x += x_increment

        self.canvas.create_line(110, 250, 110, 0, fill="black", arrow=tk.LAST)  
        self.canvas.create_line(110, 250, 400, 250, fill="black", arrow=tk.LAST)  

root = tk.Tk()
app = TemperatureApp(root)

root.mainloop()