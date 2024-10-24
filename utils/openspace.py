from table import Table,Seat
import random

class Openespace:

    def __init__(self) -> None:
        self.tables=[None]*6
        self.number_of_tables=6
    
        pass 



    def organize(self,name:str)-> None:
        
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
    
    
    def display(self)->None:

        for table in range(6):
            print(f"on Table {table+1} set the folwoing people: /n ")
            for seat in range(4):
                print(f"{seat+1} - {self.tables[table].seats[seat].occupant }")
   
   
   
    def store (file:str)->None:
        
            


