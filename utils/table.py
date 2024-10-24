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

    def __str__(self)-> str:
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

class Table():
    """A class that represents tables with 4 seats
    
    Attributes : 
    -----------
    
    seat_list : list
        A list of the Seat object assigned to the table
    
    capacity : int
        The number of seats in one table (here it is 4)
    """
    def __init__(self, list_of_seats :Seat ) -> None:
        """
        Initializes a Table object
        
        Parameters : 
        -----------
        
        """
        self.seat_list= []
        self.capacity = 4
    
    def __str__(self)-> str:



    def has_free_spot(self)-> bool:
        return self.capacity >  len(self.seat_list)
    

    def assign_seat(self,name:str)-> None:
        New_comer = Seat(name)
        if self.capacity >  len(self.seat_list):
            self.seat_list.append(New_comer)
        else:
            print("No more capacit on this table")
    
    def left_capacity (self)-> int:
        return self.capacity - len(self.seat_list)

