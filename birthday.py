from datetime import datetime
from field import Field

class Birthday(Field):

    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, '5d.%m.%Y' )
        except ValueError:
             raise ValueError("Invalid date format. Use DD.MM.YYYY")
    