import pandas as pd
from utils.openspace import Openespace




file ='bouman_8.xlsx'

df =pd.read_excel(file)


one_dim_list=['Fatemeh', 'Mohamad', 'Celina', 'Aleksander', 'David', 'Miriam', 'Olha', 'An', 'Dhanya', 'Andrii', 'Therese', 'Edoardo', 'Oscar', 'Frank', 'Beatriz', 'Kevin J', 'Patrick', 'Manel', 'Jessica', 'Vera', 'Imad', 'Kevin P', 'Patrycja', 'Nina', 'Karthika', 'Elsa', 'Nicole', 'Stef', 'Maxim', 'Boitumelo', 'Jean', 'Yassine']

O1= Openespace()

O1.organize("Hussain")
