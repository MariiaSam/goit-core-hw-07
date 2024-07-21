from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]


    def edit_phone(self, old_phone, new_phone):
        try:
            validated_phone = Phone(new_phone)
        except ValueError as e:
            raise ValueError(f"New phone number is invalid: {e}")

        self.remove_phone(old_phone)
        self.phones.append(validated_phone)


    def find_phone(self, phone):
        for p in self.phones:
             if p.value == phone:
                return p
