import csv
FILENAME = "arptable.csv"


def display_menu():
    print("Welcome to the arp entries application")
    print()
    print("list - List Entries")
    print("add - Add Entry")
    print("delete - Delete Entries")
    print("exit - exit")

def read_entries():
    arpentries = []
    with open(FILENAME, newline = "") as file:
        reader = csv.reader(file)
        for row in reader:
            arpentries.append(row)
    return arpentries



def list_entries(arpentries):
    if arpentries:
        for i, entry in enumerate(arpentries, start=1):
            print(f"{i}.{', '.join(entry)}")
    else:
        print("no entries found")


def add_entry(arpentries):
    ip_add = input("please enter an IP ADDRESS: ")
    mac_add = input("please enter a max address: ")
    entry = [ip_add,mac_add]
    arpentries.append(entry)
    print("Entry added to list")




def delete_entries(arpentries):
    index = int(input('Which number do you want to delete?: '))
    if index < 1 or index > len(arpentries):
        print("invalid entry number")
    else:
        entry = arpentries.pop(index - 1)
        print("entry was deleted")



def write_entries(arpentries):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(arpentries)
        write_entries(arpentries)

def main():
    arpentries = []
    while True:
        display_menu()
        usercmd = input("Please enter an option: ")
        match usercmd:
            case "list":
                list_entries(arpentries)
            case "add":
                add_entry(arpentries)
                write_entries(arpentries)
            case "delete":
                delete_entries(arpentries) 
            case "exit":
                break
            case _:
                print("not a valid command , Please try agin\n")
                

if __name__ == "__main__":
    main()