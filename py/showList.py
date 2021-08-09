import tkinter as tk
import pickle

with open("py\obj.pickle", "rb") as f:
    lista = pickle.load(f)

root = tk.Tk()

height = len(lista[0])
width = len(lista)
for i in range(height): #Rows
    for j in range(width): #Columns
        b = tk.Entry(root, text="")
        b.grid(row=i, column=j)
        b.insert(tk.END, lista[i][j])
    
root.mainloop()
