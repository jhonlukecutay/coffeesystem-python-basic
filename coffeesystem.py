from ast import While
from os import system
itemStock = []

start = True
while start:
    print("------------------------------------------------------")
    print("""
    Welcome to Coffee Shop!
    List of our coffees that are available: """)
    print("""   """, itemStock)
    print("""
    1 = Add a Coffee Item
    2 = Add Multiple Coffee Items
    3 = Delete an item from the shop
    4 = Examine the system list / Double insertion check
    5 = Sort items.
    """) ; print("")
    try:
        ui_input = int(input("Type here: ")) ; print("")
        
        #Append 
        if ui_input == 1:
            print("------------------------------------------------------")
            print("Type the coffee item you want to add:")
            input_name = input()
            itemStock.append(input_name)
            print("")
            print("The item have been added to the list.")
            start == True

        #Extend
        if ui_input == 2:
            print("------------------------------------------------------")
            print(itemStock)
            print("")

            try:
                input_int = int(input("How many items do you want to add: "))
                print("Please enter below the items you want to add:")

                for i in range(input_int):
                    inputMulti = input()
                    itemStock.extend([inputMulti])
                
                print("The items have been added to the list.")
                start == True

            except:
                print("Invalid Input. Try Again")
        
        #Remove 
        if ui_input == 3:
            print("------------------------------------------------------")
            print(itemStock) ; print("")
            print("(Copy the name of the item you want to delete. ex. \"Mocha\":)")
            try:
                itemRemove = input()
                itemStock.remove(itemRemove)
                print("------------------------------------------------------")
                print("The item has been removed.")
                start == True
            except:
                print("------------------------------------------------------")
                print("Sorry but there was no item named \"", itemRemove, "\" on the list.")      
        
        #Count
        if ui_input == 4:
            #If list is empty
            if not itemStock:
                print("The list is empty.")
                start == True
                continue
            print("------------------------------------------------------")
            print(itemStock)
            print("")
            print("Type the name you want to examine: ")
            x_count = input()
            print("------------------------------------------------------")
            print("The number of items that are available is: ", itemStock.count(x_count))
            start == True

        #Sort (Sort & Reverse)
        if ui_input == 5:
            print("""Choose how you want to sort the items: 
            1. Sort Alphabetically (Ascending)
            2. Sort Alphabetically (Descending)
            """)
            try:
                inputsort = int(input("Type here: "))
                if inputsort == 1:
                    itemStock.sort()
                if inputsort == 2:
                    itemStock.reverse()
                print("------------------------------------------------------")
                print("The items have been sorted successfully.")
            except:
                print("Invalid input.")

    except:
        print("Invalid Input.")