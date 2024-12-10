import tkinter as tk 
from tkinter import ttk

#the callback functions
def click_button1():
    root.title("you clicked the button")

def click_button2():
    root.destroy()

#how to create an empty root window
root = tk.Tk()
root.title("Future Value Calculator")
root.geometry("300x200")

#An empty root window 
frame = ttk.Frame(root,padding = '10 10 10 10 ')
frame.pack(fill=tk.BOTH, expand=True)

#how to two buttons to the frame 

button1 = ttk.Button(frame, text ="click me",command = click_button1)
button2 = ttk.Button(frame, text ="No,click me", command = click_button2)

#how to display buttons
button1.pack()
button2.pack() 



#how to make the window visable
root.mainloop()
#this main loop is a method 
