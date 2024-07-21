from collections import UserDict
from record import Record

class AddressBook(UserDict):

    def add_record(self, record: Record):
        if record.name.value in self.data:
            raise KeyError(f"Record with name {record.name.value} already exists")
        else:
            self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name not in self.data:
             raise KeyError(f"Record with name {name} not found")
        else:
            del self.data[name]

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())
