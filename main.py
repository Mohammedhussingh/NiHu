import pandas as pd
from utils.openspace import Openspace
import random


"""
    The main function that serves as the entry point for the open space seating program.

    This function initializes the classes responsible for seat and table assignment, 
    randomizes the seating arrangement, and provides a user interface for managing 
    and viewing seat allocations. It interacts with other parts of the program to 
    ensure that individuals are assigned to tables and seats randomly each time 
    the program runs. And here the UI that contains the functions of our program


    if you have Non on the seats  that means that some are waitning outside(for some reason we dont why know may be a call and we just try to make our project more randomized !) you fill your room by entering 1 again 
    
    """



Openspace_init = Openspace()

print("Welcome to Nihu project tp assign the guests !\n  ")
while True:
    
    print(
    "\n Select an option :\n 1- Assign the student and the couches randomly to seats \n 2-store them to excel file \n 3-Set a person to a specified position \n 4-Dispaly the disterbution of student \n Anything else to termanite !"
)


    choice = input("Your choice is : ")

    if choice == "1":  # first choice to assign the persons and print it
        file = "bouman_8.xlsx"
        df = pd.read_excel(file)
        list_of_names = df.iloc[:, 0].tolist()

        for person in list_of_names:
            Openspace_init.organize(person)  # use the organise function

        Openspace_init.display()  # print the names
        print("\n \n \n  ")
        print("\n \n \n  ")
        print("\n \n \n  ")
       
    elif choice == "2":  # second choice to store the organisation in an excel file
        file = "bouman_8.xlsx"

        df = pd.read_excel(file)
        list_of_names = df.iloc[:, 0].tolist()
        list_of_names
        for person in list_of_names:
            Openspace_init.organize(person)

        Openspace_init.store("Openspace_text.xlsx")

    elif (
        choice == "3"
    ):  # choice three to set a specified person to a specified position
        name = str(input("Enter the name of the guest:  "))
        table = int(input("Select the table (1-6): "))
        while table < 1 or table > 6:
            print("Invalid input. Please select a table between 1 and 6.")
            table = int(input("Select the table (1-6): "))

        # Get valid seat input
        seat = int(input("Select the seat (1-4): "))
        while seat < 1 or seat > 4:
            print("Invalid input. Please select a seat between 1 and 4.")
            seat = int(input("Select the seat (1-4): "))
        Openspace_init.tables[table - 1].seats[seat - 1].remove_occupant()
        Openspace_init.tables[table - 1].seats[seat - 1].occupant = name
        
    elif choice == "4":  # choice four to display
        print("\n \n \n  ")
        Openspace_init.display()

    else:
        print("Thank you for using or program !")
        break
