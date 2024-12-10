import tkinter
import yfinance as yf
import pandas as pd
def clear_treeview(treeView):
    for row in treeView.get_children():
        treeView.delete(row)
def make_selection(treeView, number, period_combobox, interval_combobox):
    if number.get() == 1:
        column_headings = ['Datetime', 'Open', 'Close']
        col_anchor = ['center', 'center', 'center']
        period_combobox.config(state = "readonly")
        interval_combobox.config(state = "readonly")
    elif number.get() == 2:
        column_headings = ['Holder', 'Shares', 'Date Reported']
        col_anchor = ['w', 'e', 'center']
        period_combobox.config(state = tkinter.DISABLED)
        interval_combobox.config(state = tkinter.DISABLED)
    clear_treeview(treeView)    
    for index, col in enumerate(column_headings):
        treeView.heading(index, text = col)
        treeView.column(index, anchor=col_anchor[index]) 

def entry_click(event, initial_message):
    if event.widget.get() == initial_message:
        event.widget.delete(0, tkinter.END)
        
def get_data(tree, symbol_entry, number, period_combobox, interval_combobox):
    clear_treeview(tree)
    ticket = yf.Ticker(symbol_entry.get())
    if ticket.institutional_holders is None:
        symbol_entry.insert(0, "*")
        symbol_entry.insert(tkinter.END, "*")
        return
    if number.get() == 1:
        period = period_combobox.get()
        interval = interval_combobox.get()
        data = ticket.history(period = period, interval = interval)
        if data.empty == False:
            data.reset_index(inplace = True)
            dataset = data[['Datetime', 'Open', 'Close']].copy()
            dataset['Datetime'] = dataset['Datetime'].dt.strftime("%Y-%m-%d %H:%M")
            dataset[['Open', 'Close']] = dataset[['Open', 'Close']].applymap(lambda x: '{0:.4f}'.format(x))
        else:
            dataset = pd.DataFrame()
    elif number.get() == 2:
        dataset = ticket.institutional_holders[['Holder', 'Shares', 'Date Reported']].copy()
        dataset['Date Reported'] = dataset['Date Reported'].dt.date
    for index in range(len(dataset)):
        #https://tkdocs.com/tutorial/tree.html
        tree.insert('', tkinter.END, values=list(dataset.loc[index]))

