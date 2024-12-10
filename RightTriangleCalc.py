import tkinter as tk 
from tkinter import ttk 
import math

class TriFrame(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent, padding = "10 10 10 10")
        self.pack()

        self.side1 = tk.StringVar()
        self.side2 = tk.StringVar()
        self.hypotenus= tk.StringVar()

        ttk.Label(self, text ="Side 1: ").grid(column =0, row=0, sticky =tk.E)
 
        ttk.Entry(self, width=30, textvariable= self.side1).grid( column=1, row=0)
        
        ttk.Label(self, text ="Side 2: ").grid(column =0, row=1, sticky =tk.E)
        
        ttk.Entry(self, width=30, textvariable= self.side2).grid( column=1, row=1) 
        
        ttk.Label(self, text ="Hypotenuse: ").grid(column =0, row=2, sticky =tk.E)
        
        ttk.Entry(self, width=30, textvariable= self.hypotenus, state ="readonly").grid( column=1, row=2)
        
        ttk.Button(self,text = "Calculate", command=self.calculate).grid(column = 1, row = 3, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5,pady=5)


    def calculate(self):
        side1 = float(self.side1.get())
        side2 = float(self.side2.get())

        hypotenus = float(math.sqrt(side1**2 + side2**2))

        self.hypotenus.set(hypotenus)

if __name__ == "__main__":
 
    root = tk.Tk()
    
    root.title("The Right Angle Triangle Calculator")
    
    TriFrame(root)
    
    root.mainloop()