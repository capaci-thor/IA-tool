import tkinter as tk


def on_configure(event):

    canvas.configure(scrollregion=canvas.bbox('all'))


root = tk.Tk()


canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill='y')

canvas.configure(yscrollcommand = scrollbar.set)

canvas.bind('<Configure>', on_configure)

frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

with open("py\Apriory_datos.txt", "r") as f:
    tk.Label(frame, text=f.read()).pack()


root.mainloop()