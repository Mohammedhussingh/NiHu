import pandas as pd
from table import Table,Seat
import random

class Openespace:
    """A class that rapresents an openspace with 6 tables
    
    Attributes : 
    -----------
    
    tables : list
        A list of Table objects that are representing the tables in the openspace
    number_of_tables : int
        The number of tables in the openspace
    """

    def __init__(self) -> None:
        """
        Initializes the Openespace object
        """
        self.tables=[None]*6
        self.number_of_tables=6
    
        pass 



    def organize(self,name:str)-> None:
        """
        Assigns a person to a random free seat on a ramdon table. Tells if all the tables are occupied.

        Parameters:
        -----------
        name : str
            The name of the person who is assigned to the seat
        """
        
        check_index= 0

        while(True):

            check_index+=1
            if check_index==24:
                print("All tables are occupied ! You can wait until you get an empty seat!")
                return
            
            Random_table = random.randint(0, 5)

            if self.tables[Random_table].has_free_spot():
                seat_number=self.tables.assign_seat(name)
                print (f"Assigned to table{ Random_table + 1 } on seat # {seat_number +1}")
                return
            
            return
        return
    
    
    def display(self) -> None:
        """
        Displays the repartition of the persons on the openspace in the tables and seats
        """

        for table in range(6):
            print(f"on Table {table+1} set the folwoing people: /n ")
            for seat in range(4):
                print(f"{seat+1} - {self.tables[table].seats[seat].occupant }")
   
   
   
    def store (self, file:str) -> None:
        """
        Stores the """
        data = {f"Table {i+1}": [] for i in range(6)}
        for table_number in range(6):
            for seat_number in range(4):
                if seat_number < len(self.tables[table_number].seat_list):
                    occupant = self.tables[table_number].seat_list[seat_number].occupant
                data[f"Table {table_number + 1}"].append(occupant)
        
    
        df = pd.DataFrame(data)
        df.to_excel(file, index=False)

Openespace.store('Openespace_repartition.xlsx')
