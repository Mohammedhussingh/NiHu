from .table import Table, Seat
import random
import pandas as pd


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

        self.tables = [Table() for _ in range(6)]
        self.number_of_tables = 6

    def __str__(self) -> str:
        """
        Returns a string of the openspace's status

        Returns :
        --------
        str
            A string that tells you number of people in room
        """

        available_seats = sum(table.left_capacity() for table in self.tables)
        return f"The capacity of the room is {available_seats}"

    def organize(self, name: str) -> None:

        check_index = 0

        while True:

            check_index = check_index + 1
            if check_index == 24:
                print(
                    "All tables are occupied ! You can wait until you get an empty seat!"
                )
                break

            Random_table = random.randint(0, 5)

            if self.tables[Random_table].has_free_spot():
                seat_number = self.tables[Random_table].assign_seat(name)
                # print (f"Assigned to table{ Random_table + 1 } on seat # {seat_number +1}")
                break
            return
        return

    def display(self) -> None:
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
        return

    def store(self, file_name: str) -> None:
        """
        Store the repartition of the person on the openspace in an excel file

        Parameters :
        -----------

        file_name : str
            The name of the file we are creating with the repartition of the persons in the openspace

        """

        data = {f"Table {i+1}": [] for i in range(6)}
        for table in range(6):
            for seat in range(4):
                occupant = self.tables[table].seats[seat].occupant
                data[f"Table {table + 1}"].append(occupant)

        df = pd.DataFrame(data)

        df.to_excel(file_name, index=False)
