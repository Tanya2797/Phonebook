import csv
from phonebook_app.models import Contact

def import_contacts():
    with open('phonebook_app/data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            name, number = row
            contact = Contact(name=name, number=number)
            contact.save()

if __name__ == '__main__':
    import_contacts()

