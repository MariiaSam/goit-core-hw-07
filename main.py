from addressBook import AddressBook
from record import Record

# Створення нової адресної книги
book = AddressBook()
print('1', book)

# Створення запису для John
john_record = Record("John")
print('2', john_record) # Contact name: John, phones: 

john_record.add_phone("1234567890")
print('3', john_record) # Contact name: John, phones: 1234567890

john_record.add_phone("5555555555")
print('4', john_record) # Contact name: John, phones: 1234567890; 5555555555

# Додавання запису John до адресної книги
book.add_record(john_record)
print('5', book) # Contact name: John, phones: 1234567890; 5555555555

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
print('6', jane_record) # Contact name: Jane, phones: 

jane_record.add_phone("9876543210")
print('7', jane_record) # Contact name: Jane, phones: 9876543210

book.add_record(jane_record)
print('8', book) # Contact name: John, phones: 1234567890; 5555555555 Contact name: Jane, phones: 9876543210
     
# Знаходження та редагування телефону для John
john = book.find("John")
print('9', john) # Contact name: John, phones: 1234567890; 5555555555
john.edit_phone("1234567890", "1112223333")
print('10', john)  # Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print('11', f"{john.name}: {found_phone}")  # John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print('12', book) # Contact name: John, phones: 1112223333; 5555555555

