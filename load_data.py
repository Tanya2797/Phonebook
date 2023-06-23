import setenv
from phonebook_app.models import Contact
import csv
from phonebook_app.models import Contact

def load_data():
    with open('phonebook_app/data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            number = row['number']
            contact = Contact(name=name, number=number)
            contact.save()

if __name__ == '__main__':
    load_data()
