from table import Table,Seat
import random



class Openespace:

    def __init__(self) -> None:
        self.tables= [Table() for _ in range(6)] 
        self.number_of_tables=6
        
    
       



    def organize(self,name:str)-> None:
        
        check_index= 0

        while(True):

            check_index=check_index+1
            if check_index==24:
                print("All tables are occupied ! You can wait until you get an empty seat!")
                break
            
            Random_table = random.randint(0, 5)

            if self.tables[Random_table].has_free_spot():
                seat_number=self.tables[Random_table].assign_seat(name)
                #print (f"Assigned to table{ Random_table + 1 } on seat # {seat_number +1}")
                break
            return
        return
    

    def display(self)->None:
        for table in range(6):
            print(f"on Table {table+1} set the folwoing people: ")
            for seat in range(4):
                print(f"{seat+1} - {self.tables[table].seats[seat].occupant }")
   
   
   
    def store (file:str)->None:
        
            return
    



list_of_names=['Fatemeh', 'Mohamad', 'Celina', 'Aleksander', 'David', 'Miriam', 'Olha', 'An', 'Dhanya', 'Andrii', 'Therese', 'Edoardo', 'Oscar', 'Frank', 'Beatriz', 'Kevin J', 'Patrick', 'Manel', 'Jessica', 'Vera', 'Imad', 'Kevin P', 'Patrycja', 'Nina', 'Karthika', 'Elsa', 'Nicole', 'Stef', 'Maxim', 'Boitumelo', 'Jean', 'Yassine']
Openespace_init= Openespace()
for person in list_of_names:
    Openespace_init.organize(person)


Openespace_init.display()
    

'''O1= Openespace()
O1.organize("Hussain")
O1.display()
'''

