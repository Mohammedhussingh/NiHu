import pandas as pd
from utils.openspace import Openespace





file ='bouman_8.xlsx'

df =pd.read_excel(file)


list_of_names=['Fatemeh', 'Mohamad', 'Celina', 'Aleksander', 'David', 'Miriam', 'Olha', 'An', 'Dhanya', 'Andrii', 'Therese', 'Edoardo', 'Oscar', 'Frank', 'Beatriz', 'Kevin J', 'Patrick', 'Manel', 'Jessica', 'Vera', 'Imad', 'Kevin P', 'Patrycja', 'Nina', 'Karthika', 'Elsa', 'Nicole', 'Stef', 'Maxim', 'Boitumelo', 'Jean', 'Yassine']

Openespace_init= Openespace()

for person in list_of_names:
    Openespace_init.organize(person)

Openespace_init.display()
    