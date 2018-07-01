"""
This program imports contacts.csv
Users are able to view a contact, list all contacts, add or delete a contact. 
"""

import csv
FILENAME = "contacts.csv" ##imports contacts.csv


##writes inforation to csv file
def write_contacts(contacts):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(contacts)
        
##reads information from csv file      
def read_contacts():
    contacts = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            contacts.append(row)
    return contacts

##Display menu options
def display():
    print("Contact Manager\n")
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")
    

##displays a list of contacts
def list_contacts(contacts):
    for i in range(len(contacts)):
        contact = contacts[i]
        print(str(i+1) + ". " + contact[0])
        
        
##adds a contact        
def add_contacts(contacts):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    contact = []
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contacts.append(contact)
    write_contacts(contacts)
    print(name + " was added.\n")
    
    
    
##delete contact with validation

def delete_contact(contacts):
    index = int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("Please enter a valid number")
    else:
        contact = contacts.pop(index - 1)
        write_contacts(contacts)
        print(contact[0] + " was deleted.\n")



##view contact with validation

def view_contact(contacts):
    index = int(input("Number: "))
    if index < 1 or index > len(contacts):
        print("Please enter a valid number")
    else:
        print(contacts[index - 1])

##main funtion
def main():
    display()
    contacts = read_contacts()
    while True:
        command = input("\nCommand: ")
        if command.lower() == "list":
            list_contacts(contacts)
        elif command.lower() == "add":
            add_contacts(contacts)
        elif command.lower() == "del":
            delete_contact(contacts)
        elif command.lower() == "view":
            view_contact(contacts)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye")
    
    
    
if __name__=="__main__":
    main()