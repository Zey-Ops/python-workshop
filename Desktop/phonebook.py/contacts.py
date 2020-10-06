from contacts import add
from contacts import find
from contacts import delete
print("***********************************")
print("Welcome to the phonebook application")
print("***********************************")
def myProgam(): 
    print("1.Find phone number")
    print("2. Insert a phone number")
    print("3. Delete a person from the phonebook")
    print("4. Terminate")
    option = input("Select operation on Phonebook App (1/2/3/4)")
    if not option.isnumeric() or (not int(option)  in (1,2,3,4)) :
        print("*********************************")
        print("Please enter a integer (1/2/3/4) :")
        print("*********************************")
        myProgam()  
    else:
        option =int(option)
    if option == 1:
        name = input("Find the phone number of :")
        print(find(name))
    elif option ==2:
        name = input("Insert name of the person :")
        number = input("Insert phone number of the person: ")
        print(add(name,number))
    elif option==3:
        name = input("Whom to delete from phonebook :")
        if delete(name) :
            print(f"Deleted name {name} successfully")
        else:
            print("Something Went wrong please try again later")
    elif option ==4:
        exit()
while True:
    myProgam()