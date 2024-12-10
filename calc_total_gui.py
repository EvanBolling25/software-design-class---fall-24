#!/usr/bin/env python3
import tkinter as tk 
from tkinter import ttk 

class CalcFrame(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent, padding = "10 10 10 10")
        self.pack()

        #define string variables for text entry
        self.retail__price = tk.StringVar()
        self.quantity = tk.StringVar()
        self.total = tk.StringVar()


        #display the grid of componets 
        ttk.Label(self, text ="Retail Price: ").grid(column =0, row=0, sticky =tk.E)
        ttk.Entry(self, width=30, textvariable= self.retail__price).grid( column=1, row=0)

        ttk.Label(self, text ="Quantity: ").grid(column =0, row=1, sticky =tk.E)
        ttk.Entry(self, width=30, textvariable= self.quantity).grid( column=1, row=1) 

        ttk.Label(self, text ="Total: ").grid(column =0, row=2, sticky =tk.E)
        ttk.Entry(self, width=30, textvariable= self.total, state ="readonly").grid( column=1, row=2)

        ttk.Button(self,text = "Calculate", command=self.calculate).grid(column = 1, row = 3, sticky=tk.E)

        #add padding to all compoents 

        for child in self.winfo_children():
            child.grid_configure(padx=5,pady=3)


    def calculate(self):
        #get the numbers from the first two text entry feilds
        retail_price = float(self.retail__price.get())
        quantity = int(self.quantity.get())

        #calculate the total
        total = retail_price * quantity 

        #display the total in the third text feild 
        self.total.set(total)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("The Calculate Total Program")
    CalcFrame(root)
    root.mainloop()