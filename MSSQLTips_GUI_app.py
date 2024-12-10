import tkinter
from tkinter import ttk 
import pandas as pd 
import yfinance as yf 
import MSSQLTips_GUI_backend as backend

#creating the main GUI window 
root = tkinter.Tk()
root.title("MSSQLtips Finance")
root.geometry('420x460+300+300')
root.resizable(0,0)
#3 add widgets to the frame 
#3.1 creates frames 
greeting_frame = tkinter.Frame(root)
textbox_frame = tkinter.Frame(root)
radio_frame = tkinter.LabelFrame(root, text = "Select a dataset")
combobox_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
treeview_frame = tkinter.Frame(root)
#3.2 arranges the frames 
greeting_frame.pack()
textbox_frame.pack()
radio_frame.pack()
combobox_frame.pack()
button_frame.pack()
treeview_frame.pack()
#3.3 uses the greeting frame to organize widgets
#3.3.1 adds a label to the greeting frame
greeting_label = tkinter.Label(greeting_frame, text = "Welcome to MSSQLTips")
#3.3.2 arranges the label
greeting_label.pack()
#3.4 Arrange the textbox frame 
#3.4.1 adds a lebel to the textbox frame 
entry_label = tkinter.Label(textbox_frame, text ="Stock ticker Symbol:")
greeting_label.config(text = "Please Enter Stock Ticker Symbol:")
#3.4.2 adds a text box to the textbox frame and set the initial value
text_entry = tkinter.Entry(textbox_frame)
initial_value = "GOOG"
text_entry.insert(0,initial_value)
text_entry.delete(0,tkinter.END)
text_entry.insert(0,"AAPL")
text_entry.get()
text = tkinter.StringVar(textbox_frame)
text_entry = tkinter.Entry(textbox_frame, textvariable= text)
text.set("GOOG")
text.get()
#3.4.3 defines teh frame layout
entry_label.pack(side = tkinter.LEFT)
text_entry.pack(side = tkinter.LEFT)
#3.4.4 Bind to the event
text_entry.bind("<ButtonPress-1>", lambda event, initial_message = initial_value: backend.entry_click(event, initial_value))
#3.5 arranges the radio frame 
#3.5.1 set inital value 
number = tkinter.IntVar()
number.set(1)
#3.5.2 adds radio buttons to the radio frame. on selection we can display the value using one label 
radio_historical_data = tkinter.Radiobutton(radio_frame, text = "Historical Data", value = 1, variable = number, command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))
radio_institutional_holders = tkinter.Radiobutton(radio_frame, text ="institutional Holders", value = 2, variable = number,command = lambda:backend.make_selection(tree, number, period_combobox, interval_combobox))



#3.5.3 Defines the frame layout
radio_historical_data.grid(row=0,column=0)
radio_institutional_holders.grid(row=0,column=1)
#3.6 arrangges the combobox frame
#3.6.1 add labels, comboboxes and the get button to the frame
period_label = tkinter.Label(combobox_frame, text = "Period:")
period_combobox = ttk.Combobox(combobox_frame, value =['1d','5d','1mo'], state = "readonly")
interval_label = tkinter.Label(combobox_frame, text="Interval:")
interval_combobox = ttk.Combobox(combobox_frame, value=['15m','30m','1h'], state="readonly")
#3.6.2 Set default selection.
period_combobox.current(0)
interval_combobox.current(0)
#3.6.3 Define the frame layout
period_label.grid(row=0, column=0)
period_combobox.grid(row=0, column=1)
interval_label.grid(row=0, column=2)
interval_combobox.grid(row=0, column=3)
period = period_combobox.get()
interval = interval_combobox.get()

# This function is for testing. We place all associated functions in a separated code file.
def greeting():
    greeting_label.config(text = 'You click on me.')
 
#3.7 Arrange the button frame.
#3.7.1 Adds a button to the button frame.
#3.7.1 Adds a button to the button frame.
get_button = tkinter.Button(button_frame, text = "Get Data", command = lambda:backend.get_data(tree, text_entry, number, period_combobox, interval_combobox))

#3.7.2 Defines the frame layout.
get_button.pack()

#3.8 Arrange the treeview frame.
#3.8.1 Adds a treeview to the treeview frame.
columns = ['col0','col1','col2']
default_headings = ['Datetime', 'Open', 'Close']
tree = ttk.Treeview(treeview_frame, columns = columns, show = 'headings')
# Defines the headings
for index, col in enumerate(columns):
    tree.column(col, width = 100, anchor = 'center')
    tree.heading(col, text=default_headings[index])
#3.8.2 Add a scrollbar to the treeview frame.
scrollbar = ttk.Scrollbar(treeview_frame, orient = tkinter.VERTICAL, command = tree.yview)
tree.configure(yscroll = scrollbar.set)
#3.8.3 Defines the frame layout.
tree.grid(row = 0, column = 0)
scrollbar.grid(row = 0, column = 1)
#Add a fake list to the tree
dataset = [['2023-02-14','45.23', '42.65'],
           ['2023-02-15','42.70', '48.92'],
           ['2023-02-16','22.46', '20.98']
           ]
for index in range(len(dataset)):
    tree.insert('', tkinter.END, values=dataset[index])


#4 runs the windows main loop 
root.mainloop()