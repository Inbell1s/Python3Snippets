#!/bin/python3
#
#Default Menu
#

def menu():
    try:
        print("\nWhat would you like to do?:\n")
        print("[1].")
        print("[2].")
        print("[3].")
        print("[0] Exit program.\n")
        choice = input("Option: ")
    
        if choice == "1" :
            #run 1
            print("\nStarting 1!..")
        elif choice == "2" :
            #run 2
            print("\nStarting 2!..")
        elif choice == "3" :
            #run 3
            print("\nStarting 3!..")
        elif choice == "0" :
            print("\nClosing...")
            sys.exit(0)
        else :
            print("\nWrong input try again!\n")
            menu()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Closing.")
        sys.exit(0)
    except ValueError:
        print('\nInvalid input given.\n')
        menu()

menu()
