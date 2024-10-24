class Seat:
    """"""
    def __init__(self, free : bool, occupant : str) -> None:
        self.free = free
        self.occupant = occupant

    def __str__(self)-> str:
        if self.free == True:
            return f"The seat is {self.free}"

    def set_occupant(self, name: str)-> bool:
        if self.free == True:
            self.occupant = name

    def remove_occupant(self):
        previous_occupant = self.occupant
        self.occupant = ""
        if self.free == False:
            self.free == True
        return previous_occupant

