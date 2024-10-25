import random

class Seat:
    """
    A class that represent seats that can be occupied by an occupant or free
    
    Attributes :
    -----------
    
    free : bool
        Represent if the seat is free(True) or occupied(False)
    occupant : str
        The name of the occupant of the seat, if there is one
    """

    def __init__(self, free : bool, occupant : str) -> None:
        """
        Initializes a Seat object

        Parameters :
        -----------
    
        free : bool
            Represent if the seat is free(True) or occupied(False)
        occupant : str
            The name of the occupant of the seat, if there is one
        """

        self.free = free
        self.occupant = occupant

    def __str__(self) -> str:
        """
        Returns a string of the seat's status

        Returns : 
        --------
        str
            A string that says if the seat is free or occupied and by who
        """

        if self.free == False:
            return f"The seat is for {self.occupant}"
        else:
            return "The seat is free "

    def set_occupant(self, name: str)-> None:
        """
        Puts an occupant on a seat if the seat is free
        
        Parameters :
        -----------
        
        name : str
            The name of the occupant of the seat
        
        Returns : 
        --------
        
        None
        """
        
        
        if self.free == True:
            self.occupant = name

    def remove_occupant(self):
        """Removes an occupant of a seat
        
        Returns :
        --------
        
        str
        The name of the previous occupant of the seat
        """
        previous_occupant = self.occupant
        self.occupant = ""
        if self.free == False:
            self.free == True
        return previous_occupant


class Table:
    """A class that represents tables with 4 seats
    
    Attributes : 
    -----------
    
    seats : list
        A list of the Seat object assigned to the table
    capacity : int
        The number of seats in one table (here it is 4)
    """

    def __init__(self) -> None:
        """
        Initializes the Table object
        
        Parameters : 
        -----------
        
        seats : list
            A list of the Seat objects assigned to the table
    
        capacity : int
            The number of seats in one table (here it is 4)
        """
        self.seats= [Seat(True,None) for _ in range(6)] 
        self.capacity = 4
    
    def __str__(self) -> str:
         """
        Returns a string of the Table's status

        Returns : 
        --------
        str
            A string that gives the capacity of the table
        """
         return f"The capacity is {self.capacity}"
         


    def has_free_spot(self)-> bool:
        """
        Tells if the table has a free seat
        
        Parameters : 
        -----------
        
        capacity : int
            The number of seats in one table

        Returns : 
        --------

        bool
            True if there is a free seat, False if not
        """
        return self.capacity > 0
    

    def assign_seat(self,name:str)-> int:
        """
        Assigns a person to a seat in the table if there is a free seat. If not, says that there is no more capacity on the table
        
        Parameters :
        -----------
        
        name : string
             name of the person who is assigned to the seat
        """
        New_comer = Seat(False,name)
    
        while(True):
            Random_seat = random.randint(0, 3)
            
            if 0 <  self.capacity and self.seats[Random_seat].free :
                self.seats[Random_seat]=New_comer
                self.capacity=self.capacity-1
               
                
                return Random_seat

            elif 0<  self.capacity:
                continue
            else:
                print("No more capacity on this table")
                break
        
    def left_capacity (self) -> int:
        """
        Tells how many seats are left in the table

        Parameters : 
        -----------
        
        capacity : int
            The number of seats in one table

        Returns : 
        --------

        int
            The number of seats that are left in the table
        """
        return (self.capacity)




table= Table()
table.assign_seat("nina")
table.assign_seat("hussain")
print(table)


