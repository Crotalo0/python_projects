# Progetto 6 : Contact Book
from os import path


class ContactBook:
    
    def __init__(self):
        
        # Setting a path instance with None 
        self.path = None
        
        # Creating the main dictionary template.
        self.contact_list = {
            'Names':[], 
            'Surnames':[], 
            'Phones':[], 
            'Emails':[]            
            }
        
        # Temporary string utilized in del_contact
        self. temp_str = ''
        
    def create_cb(self, path):
        """Create contact book file."""
        self.path = path
        f = open(path, 'w')
        f.close()
            
    
    def  open_cb(self, path):
        """Opening cb file"""
        self.path = path
        
        # Writing the content of the path file into the dictionary
        with open(path, 'r') as f:
            for line in f:
                name, surname, phone, email = line.split(';')
                
                # Filling the lists with the values drom the file.
                self.contact_list['Names'].append(name)
                self.contact_list['Surnames'].append(surname)
                self.contact_list['Phones'].append(phone)
                self.contact_list['Emails'].append(email)
    
    def add_contact(self, name, surname, phone, email):
        """Add a contact to ContactBook class."""
        self.contact_list['Names'].append(name)
        self.contact_list['Surnames'].append(surname)
        self.contact_list['Phones'].append(phone)
        self.contact_list['Emails'].append(email)
        # Writing to file elements of lists.
        with open(self.path, 'a') as f:
            f.write(f'{name};{surname};{phone};{email}\n')
            
    
    def del_contact(self, name, surname, phone, email):
        """Delete contact from file and list."""
        # Removing from lists 
        self.contact_list['Names'].remove(name)
        self.contact_list['Surnames'].remove(surname)
        self.contact_list['Phones'].remove(phone)
        
        # Removing last element from list plus \n, because last element has that appended.
        self.contact_list['Emails'].remove(email + '\n')
        
        # Starting file manupulation.
        with open(self.path, 'r') as f:
            
            # Writing the content of the cb into the temporary string as a list.
            self.temp_str = f.readlines()
            
            # Cycling the list.
            for string in self.temp_str:
                
                #If the element of temp_str is equal to the same formatted string with the entry to delete, remove the list element.
                if string == f'{name};{surname};{phone};{email}\n':
                    self.temp_str.remove(string)
         
        # Rewriting the file with the entry not deleted.           
        with open(self.path, 'w') as f:
            for line in self.temp_str:
                f.write(line)  
    
    def modify_contact(self, old_name, old_surname, old_phone, old_email, new_name, new_surname, new_phone, new_email):
        """Calling del and add to delete entry and recreate with correct entry."""
        self.del_contact(old_name, old_surname, old_phone, old_email)
        self.add_contact(new_name, new_surname, new_phone, new_email)
        
    def search_contact(self, keyword):
        """Search engine with keywords."""
        
        # While argument
        done = False
        
        # while cycle to select search keyword
        while not done:
            if keyword == '1':
                key = 'Names'
                done = True
            elif keyword == '2':
                key = 'Surnames'
                done = True
            elif keyword == '3':
                key = 'Phones'
                done = True
            elif keyword == '4':
                key = 'Emails'
                done = True
            else:
                print('Please provide a valid entry. ')
        
        # Creating a 'name' with the specific keyword we want to search. Ex: after selecting 1- > Names, name takes the name I wanna search.       
        name = input(f"Select '{key}' entry  to search: ")
        
        # If the specific keyword is in the list proceed with printing, otherwise execute the else.
        if name in self.contact_list:
            elem_index = self.contact_list[key].index(name)
            return f"Name: {self.contact_list['Names'][elem_index]}, Surname: {self.contact_list['Surnames'][elem_index]}, Phone: {self.contact_list['Phones'][elem_index]}, Email: {self.contact_list['Emails'][elem_index]}"
        else:
            return "There is no entry for this keyword."
        
    def __str__(self):
        """Standard print when calling print(ContactBook)."""
        new_str = ''
        for i in range(len(self.contact_list['Names'])):
            new_str = new_str + f"{i+1}) Name: {self.contact_list['Names'][i]}, Surname: {self.contact_list['Surnames'][i]}, Phone: {self.contact_list['Phones'][i]}, Email: {self.contact_list['Emails'][i]}"
        final_str = f"Number of contacts: {len(self.contact_list['Names'])}" +'\n'+ new_str 
        return final_str

def main():
    """Main program."""
    # Creating a ContactBook() instance
    cb = ContactBook()
    
    # Checking if there is an existing contactbook
    # I could add in the future the possibility to choose a specified value 
    # And maybe to create a cb with a different name
    if path.exists('mycontactbook.txt') is True:
        cb.open_cb('mycontactbook.txt')
    else:
        cb.create_cb('mycontactbook.txt')
    
    # Creating a print list for inputs.
    print("""
        What do you want to do?
        1. Add contact
        2. Delete contact
        3. Modify contact
        4. Find contact
        5. Show entire contact book 
        q. Quit
        """)   
    
    # While argument                   
    done = False
    
    while not done:
        choice = input("Enter your choice: ")
        
        # if cycle linked to the precedent print list. 
        if choice == '1':
            name, surname, phone, email = input('Input name: '), input('Input Surname:'), input('Input Phone:'), input('Input email:')
            cb.add_contact(name, surname, phone, email)
            print('New contact added.')
        
        elif choice == '2':
            name, surname, phone, email = input('Input name: '), input('Input Surname:'), input('Input Phone:'), input('Input email:')
            cb.del_contact(name, surname, phone, email)
            print('Contact deleted.')
        
        elif choice == '3':
            old_name, old_surname, old_phone, old_email = input('Input old name: '), input('Input old Surname:'), input('Input old Phone:'), input('Input old email:')
            new_name, new_surname, new_phone, new_email = input('Input new name: '), input('Input new Surname:'), input('Input new Phone:'), input('Input new email:')
            cb.modify_contact(old_name, old_surname, old_phone, old_email, new_name, new_surname, new_phone, new_email)
            print('Contact succesfully modified.')
       
        elif choice == '4':
            print("""
            Select keyword for the research: 
            1. Name
            2. Surname
            3. Phone number
            4. Email
            """) 
            search_choice = input('Enter search choice: ')
            print(cb.search_contact(search_choice))
        
        elif choice == '5':
            print('Current contact book: ')
            print(' --  --  --  --  --  --  --  --  --  --  --  --  -- ')
            print(cb)
            print(' --  --  --  --  --  --  --  --  --  --  --  --  -- ')
            print('End of contact book.\n')
        
        elif choice == 'q':
             done = True
             print('Bye')
        else:
            print('Please provide a valid entry. ')

if __name__ == "__main__":
    main()





