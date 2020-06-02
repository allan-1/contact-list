import csv

contacts_data = 'contact1.csv'
contact_value = ['Name', 'Email', 'Phone Number', 'Location']

def display_menu():
    print('----------------------------------')
    print('-------------Contacts--------------')
    print('-----------------------------------')
    print('1. Add contact')
    print('2. View contacts')
    print('3. Modify contact')
    print('4. Delete Contact')

def add_contact():
    global contact_value
    global contacts_data

    contacts_database = []

    for value in contact_value:
        data = input('Enter contacts {0} : '.format(value))
        contacts_database.append(data)

    with open(contacts_data, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows([contacts_database])
    print('contact saved sucessfully')

def view_contact():
    global contact_value
    global contacts_data

    print('----- Contact List ----------')
    
    with open(contacts_data, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for contacts in contact_value:
            print(contacts, end='| \t |')
            #print('\n')

        print('\n---------------------------------------------')
        
        for row in reader:
            for item in row:
                print(item, end='\t |')
            print('\n')
    
    input('Enter any key to exit')

def modify_contact():
    global contacts_data
    global contact_value

    name = input('Enter name to search : ')
    index = None
    updated_contacts = []

    with open(contacts_data, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if name == row[0]:
                    index = counter
                    print('Student found at index : ', index)
                    contact = []
                    for value in contact_value:
                        data = input(f'Enter contacts : {value} ')
                        contact.append(data)
                    updated_contacts.append(contact)
                else:
                    updated_contacts.append(row)
                counter += 1
    
    if index is not None:
        with open(contacts_data, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows([updated_contacts])

        print('Contact modified sucessfully')
    else:
        print(f'{name} not in contacts')


def delete_contact():
    global contacts_data
    global contact_value

    name = input('Enter name to delete : ')
    updated_contact = []
    contact_found = False

    with open (contacts_data , 'r', encoding='utf-8') as f :
        reader = csv.reader
        counter = 0

        for row in reader:
            if len(row) > 0:
                if name != row:
                    updated_contact.append(row)
                    counter += 1
                else:
                    contact_found = True
                
    if contact_found is True:
        with open(contacts_data, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(updated_contact)
        
        print('Contact deleted succesfully')
    
    else:
        print(f'{name} not in contacts')

    input('Press an key to exit ')



while True:
    display_menu()

    option = input("Enter your option  ")

    if option == '1':
        add_contact()
    elif option == '2':
        view_contact()
    elif option == '3':
        modify_contact()
    elif option == '4':
        delete_contact()

    else:
        break