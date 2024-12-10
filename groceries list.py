#wrtie a module that creates a grocery list

def display_menu():
    print("welcome to the grocey list program ")
    print()
    print("COMMAND MENU")
    print("add - add an item")
    print("remove- remove an item")
    print("view - view an item")
    print("exit - exit program")
    print()

def add_item(groceries):
    item = input("enter the item to add: ")
    groceries.append(item)

def remove_item(groceries):
    item = input("enter the item to remove: ")
    if item in groceries:
        groceries.remove(item)
    else:
        print(item, " not found in your list")
    
def view_items(groceries):
    if groceries:
        print("Your groceries list")
        for item in groceries:
            print(item)
    else:
        print("your groceries list is empty")




def main():
    groceries =[]
    #this main function displays menu to user
    #untill they exit 
    while True:
        display_menu() 
        action = input("Enter a command: ")
        if action == "add":
            add_item(groceries)
        elif action == "remove":
            remove_item(groceries)
        elif action == "view":
            view_items(groceries)
        elif action == "exit":
            break
        else:
            print("please select a valid option")




if __name__ == "__main__":
    main()
    