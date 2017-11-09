import ev3dev.ev3 as ev3
import math
import time
import json
import collections
import paho.mqtt.client as mqtt
import tkinter
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

def main():
    welcome_screen()

def welcome_screen():
    root = tkinter.Tk()
    root.title = "Indiana Jone's Adventure"

    frame1 = ttk.Frame(root, padding=20, relief='raised')
    frame1.grid()

    label = ttk.Label(frame1, justify=tkinter.LEFT, text="Welcome to Indy's Adventure")
    label.grid(columnspan=2)

    path = "C:/Users/thompsm5/Pictures/CSSE/062612-indiana-jones.jpg"
    indy = ImageTk.PhotoImage(Image.open(path))
    label1 = ttk.Label(frame1, image=indy)
    label1.grid(row=1, column=0)

    label2 = ttk.Label(frame1, justify=tkinter.LEFT, text="What is your name?")
    label2.grid(columnspan=2)

    name_entry = ttk.Entry(frame1, width=50)
    name_entry.grid(row=3, column=0)

    submit = ttk.Button(frame1, text = "Submit")
    submit.grid(row=3, column=1)
    submit['command'] = lambda: start_adventure(name_entry, root)
    root.bind('<Return>', lambda event: start_adventure(name_entry, root))

    root.mainloop()

def start_adventure(name_entry, root1):
    name = name_entry.get()
    root1.destroy()
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20, relief='raised')
    frame.grid()

    path = "C:/Users/thompsm5/Pictures/CSSE/indiana-jones-header.jpg"
    indy = ImageTk.PhotoImage(Image.open(path))
    label = ttk.Label(frame, justify=tkinter.LEFT, text="Great, " + str(name) + ", let's begin your adventure.")
    label.grid(row=0, column=0)
    label1 = ttk.Label(frame, image = indy)
    label1.grid(row=1,column=0)

    label2 = ttk.Label(frame, justify=tkinter.LEFT, text="There is tale of an ancient treasure in a hidden mystical cave.\nIndiana Jones has enlisted you to help him find the artifact.\nYou must go through three daunting tasks to find it.\nPass and you will be rewarded with treasures beyond your wildest dreams.\nFail, and you might be run over by a loose boulder.\nOr worse, attacked by snakes.\n\nAre you ready?")
    label2.grid(row=3, column=0)

    ready = ttk.Button(frame, text = "I'm Ready!")
    ready.grid(row=4, column=1)
    ready['command'] = lambda: puzzle_1(root)
    root.bind('<Return>', lambda event: puzzle_1(root))

    root.mainloop()

def puzzle_1(r):
    r.destroy()
    ev3.Sound.Speak("I am ready. Let's go.")
    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=20, relief='raised')
    frame.grid()

    solved = ttk.Button(frame, text='Solved')
    solved.grid()
    solved['command']=lambda : snakes(root)

    root.mainloop()

def snakes(r):
    r.destroy()









main()