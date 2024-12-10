#!/usr/bin/env python3

def get_miles_driven(): # creates a function called get_miles_driven that asks the user for an input how many miles theyve driven. 
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used(): # fucnction that asks the user for how many gallons of gas they used , sets the input as flot adn checks if the input is above 0 
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    more = "y" #while this loop is true , it gathers the data and then does the operations required to calulate MPG 
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ") # asks you if you would like to calculate another MPG result
    
    print("Bye")

if __name__ == "__main__": #checks if there is a fucntion named main 
    main()

