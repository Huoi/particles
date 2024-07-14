import tkinter as tk
import tkinter.ttk as ttk

class Slider:
    def __init__(self, root, lo, hi, val, text):
        self.val = tk.IntVar(root, val)

        self.label = tk.Label(root, text=text)
        self.label.pack()
        self.slider = tk.Scale(root, from_=lo, to=hi, variable=self.val, orient="horizontal", length=200)
        self.slider.set(val)
        self.slider.pack()
        self.separator = ttk.Separator(root, orient=tk.HORIZONTAL)
        self.separator.pack(fill="x")

    def get_value(self):
        return self.val.get()

class Gui:
    def __init__(self, count, speed, radius):
        self.count = count
        self.speed = speed
        self.radius = radius

        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.option_add("*Font", "consolas 20")

        self.count_slider = Slider(self.root, 10, 100, self.count, "Particle Count")
        self.speed_slider = Slider(self.root, 1, 30, self.speed, "Particle Speed")
        self.radius_slider = Slider(self.root, 1, 30, self.radius, "Particle Radius")

        self.updated = False
        tk.Button(self.root, text="Update", command=self.clicked).pack()

    def update(self):
        self.root.update()

    def quit(self):
        try:
            self.root.destroy()
        except Exception:
            pass

    def clicked(self):
        self.count = self.count_slider.get_value()
        self.speed = self.speed_slider.get_value()
        self.radius = self.radius_slider.get_value()
        self.updated = True
