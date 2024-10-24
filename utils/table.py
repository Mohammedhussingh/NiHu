
import random

class Seat:

    def __init__(self, free : bool , occupant : str) -> None:
        self.free = free
        self.occupant = occupant

    def __str__(self)-> str:
        
        if self.free == False:
            return f"The seat is for {self.occupant}"
        else:
            return "The seat is free "

    def set_occupant(self, name: str)-> None:
        if self.free == True:
            self.occupant = name


    def remove_occupant(self)-> str:
        previous_occupant = self.occupant
        self.occupant = ""
        if self.free == False:
            self.free == True
        return previous_occupant







class Table:


    def __init__(self) -> None:
        self.seats= [Seat(True,None) for _ in range(6)] 
        self.capacity = 4


    def has_free_spot(self)-> bool:
        return self.capacity > 0
    

    def assign_seat(self,name:str)-> int:
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
        
    def left_capacity (self)-> int:
        return ( self.capacity)

    


        



        