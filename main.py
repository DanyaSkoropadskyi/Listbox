import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random

class TemperatureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Температурна програма")
        self.root.geometry("500x400")

        self.temperatures = []

        label = tk.Label(root, text="Введіть температури протягом тижня (через кому):")
        label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.btn = tk.Button(root, text="Побудувати", command=self.build_graph)
        self.btn.pack(pady=5)

        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def build_graph(self):
        self.ax.clear()  # Очистка графіка перед побудовою нового

        try:
            self.temperatures = [int(temp.strip()) for temp in self.entry.get().split(",")]
            days = list(range(1, len(self.temperatures) + 1))

            # Побудова графіка
            self.ax.plot(days, self.temperatures, marker='o', linestyle='-')

            # Позначення максимальної та мінімальної температур
            max_temp = max(self.temperatures)
            min_temp = min(self.temperatures)
            self.ax.plot(days[self.temperatures.index(max_temp)], max_temp, marker='o', markersize=8, color='red')
            self.ax.plot(days[self.temperatures.index(min_temp)], min_temp, marker='o', markersize=8, color='green')

            # Позначення точок максимальних та мінімальних температур колами
            self.ax.scatter(days[self.temperatures.index(max_temp)], max_temp, color='red', s=100, zorder=3)
            self.ax.scatter(days[self.temperatures.index(min_temp)], min_temp, color='green', s=100, zorder=3)

            # Налаштування графіка
            self.ax.set_xlabel('Дні тижня')
            self.ax.set_ylabel('Температура, °C')
            self.ax.set_title('Температури протягом тижня')

            # Додавання сітки та написів на осі
            self.ax.grid(True)
            self.ax.set_xticks(days)
            self.ax.set_yticks(range(min(self.temperatures), max(self.temperatures) + 1))
            self.ax.set_xticklabels(days)
            self.ax.set_yticklabels(range(min(self.temperatures), max(self.temperatures) + 1))

            # Оновлення графіка
            self.canvas.draw()

            # Показ повідомлення з інформацією про максимальну та мінімальну температуру
            messagebox.showinfo("Інформація", f"Максимальна температура: {max_temp} °C\nМінімальна температура: {min_temp} °C")

        except ValueError:
            messagebox.showerror("Помилка", "Будь ласка, введіть коректні числа для температур")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureApp(root)
    root.mainloop()