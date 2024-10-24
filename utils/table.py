
class Seat():
    def __init__(self) -> None:
        pass
    



class Table():
    def __init__(self, list_of_seats :Seat ) -> None:
        self.seat_list= []
        self.capacity = 4


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

    


        
















        