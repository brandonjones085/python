"""
This program will allow a user to add, drop, edit, or show all the items in a list. 

"""

##displays the header and command prompts
def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

##shows all the items in the list
def list(wizard):
    i = 1
    for item in wizard:
        print(str(i) + ". " + item)
        i += 1
    print()
    
    
##this will add items to the list if there is less than four items    
def grab(wizard):
    name = input("Name: ")
    i = 1
    for item in wizard: 
        i += 1
    if i > 4: 
        print("You can only carry four items. You must drop one first")
    else:
        wizard.append(name)
        print(name, "was added")

##This function will edit an item in the list      
def edit(wizard):
    number = int(input("Number: "))
    if number < 1 or number > len(wizard):
        print("Please enter a valid number")
    else:
        name = input("Updated item: ")
        wizard.pop(number - 1)
        wizard.append(name)
        print("Item number " + str(number) + " was updated")
        
    
    
##This will delete an item from the list
def drop(wizard):

    number = int(input("Number: "))
  
    if number < 1 or number > len(wizard):
        print("Please enter a valid number")
    else:
        item = wizard.pop(number - 1)
        print(item, "was deleted")

        
def main():
    wizard_list = ['Hat', 'Wand', 'Potion']
    display_menu()
    
    while True: 
        command = input("\nCommand: ")
        if command.lower() == "show":
            list(wizard_list)
        if command.lower() == "grab":
            grab(wizard_list)
        if command.lower() == "edit":
            edit(wizard_list)
        if command.lower() == "drop" :
            drop(wizard_list)
        if command.lower() == "exit":
            break
    print("\nBye")
            
            
    
if __name__ == "__main__":
    main()