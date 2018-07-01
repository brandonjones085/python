##code

def number_of_students(first, last, full):
    number = int(input("How mainy students are in the class: "))
    for i in range(0,number):
        first_name = input("Student first name: ")
        first.append(first_name)
        last_name = input("Student last name: ")
    
        last.append(last_name)
        full.append(" ")
    print("****************************************")
    print("Students submitted: ")
    print("First names: ", first)
    print("Last names: ", last)
    print("\n******************************************")
    print("Students in the class")
    
    for i in range (0, number):
        full[i] = last[i].upper() + "," + first[i].upper()
        
        full.sort()
    for i in range(0, number):
        print(full[i])

    


def main():
    first_list = []
    last_list = []
    full_list = []
    print("Alphabetizing Student Lists\n")
    number_of_students(first_list, last_list, full_list)
    
    
if __name__=="__main__":
    main()