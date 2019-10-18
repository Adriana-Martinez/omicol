# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    nombre = Col('Name')
    email = Col('Description')
    estado= Col('Estado')
    acciones = Col('Acciones')
   
# Get some objects
class User(object):
    def __init__(self, name, description):
        self.nombre = nombre
        self.email = email
        self.estado = estado
        self.Acciones = Acciones
# Or, more likely, load items from your database with something like
items = UserModel.query.all()

# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
# or just {{ table }} from within a Jinja template