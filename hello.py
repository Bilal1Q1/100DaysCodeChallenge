from prettytable import PrettyTable
table = PrettyTable()



table.align= 'r'
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander','World'])
table.add_column('Type',['Electric', 'Water', 'fire','Hello'])
print(table)