import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import messagebox

window = tk.Tk()
window.title("Game")
window.geometry("750x400")

power = 5

colors = ["#FF4500" , "#FF1493", "#32CD32" , "#1E90FF" , "#800000"]

def ranColGen():
  ranCol = random.choice(colors)
  return ranCol

Count = 0
boba = "#FF4500"

def buy():
  global power
  global Count
  power = power + 10
  ranCol = ranColGen()
  window.configure(background=ranCol)
  button["bg"] = ranCol
  hello["bg"] = ranCol
  balance["bg"] = ranCol
  global Count
  
  if Count > 100:
    Count = Count - 100
  else:
    messagebox.showerror(message = "Не хватает деняк!!!")
  

button = tk.Button(text="𝖀𝖕𝖌𝖗𝖆𝖉𝖊!", command = buy, bg = ranColGen())
button.place(x=400, y=300)

def qwe():
  global ranCol
  global power
  global Count
  Count = Count + power
  balance["text"] = Count
  if balance == 1000:
    window.configure(background=boba)


hello = tk.Label(text="ʙᴀʟᴀɴᴄᴇ:")
hello.place(x = 280, y = 31)

s = Image.open("box.png")
c = s.resize((50, 50))
b = ImageTk.PhotoImage(c)

button = tk.Button(command = qwe , image = b)
button.place(x=323, y=150)


balance = tk.Label(text = Count)
balance.place(x = 350 , y = 31)


window.configure(background="#FFA500")

tk.mainloop()