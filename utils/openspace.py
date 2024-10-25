from table import Table,Seat
import random



class Openspace:
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
        Initializes the Openspace object

        Parameters :
        -----------

        tables : list
            A list of Table objects that are representing the tables in the openspace
        number_of_tables : int
            The number of tables in the openspace
        """

        self.tables= [Table() for _ in range(6)] 
        self.number_of_tables = 6
    
    def __str__(self):
        """
        Returns a string of the openspace's status

        Returns : 
        --------
        str
            A string that tells you 
        """
        return 

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
        """
        Displays the repartition of the persons on the openspace in the tables and seats
        
        Parameters : 

        -----------
        tables : list
            A list of Table objects that are representing the tables in the openspace
        """
        for table in range(6):
            print(f"on Table {table+1} set the folwoing people: ")
            for seat in range(4):
                print(f"{seat+1} - {self.tables[table].seats[seat].occupant }")
   
   
   
    def store (self, file:str) -> None:
        """
        Store the repartition of the person on the openspace in an excel file
        
        Parameters : 
        -----------

        file_name : str
            The name of the file we are creating with the repartition of the persons in the openspace
        
        """




list_of_names=['Fatemeh', 'Mohamad', 'Celina', 'Aleksander', 'David', 'Miriam', 'Olha', 'An', 'Dhanya', 'Andrii', 'Therese', 'Edoardo', 'Oscar', 'Frank', 'Beatriz', 'Kevin J', 'Patrick', 'Manel', 'Jessica', 'Vera', 'Imad', 'Kevin P', 'Patrycja', 'Nina', 'Karthika', 'Elsa', 'Nicole', 'Stef', 'Maxim', 'Boitumelo', 'Jean', 'Yassine']
Openspace_init= Openspace()
for person in list_of_names:
    Openspace_init.organize(person)


Openspace_init.display()