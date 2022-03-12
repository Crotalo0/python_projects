# Program from NeuralNine youtube channel.
# YT video link: https://www.youtube.com/watch?v=O8596GPSJV4

from cryptography.fernet import Fernet


class PasswordManager:
    
    def __init__(self):
        """Constructor for Password manager."""
        
        # Define a key instance to save key encryption
        self.key = None
        
        # Define a password_file with all passwords
        self.password_file = None
        
        # To store passwords to write or read from a file
        self.password_dict = {}
        
    def create_key(self, path):
        """Key encryption generator"""
        
        # generating the encryption key.
        self.key = Fernet.generate_key()
        
        #Storing the key in a file.
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        
        #Opening file in path to read the encryption key.
        with open(path, 'rb') as f:
            self.key = f.read()
            
    def create_password_file(self, path, initial_values = None):
        """Set the path to the attribute password_file."""
        
        # Giving the password file path to the init variable.
        self.password_file = path
        
        # Checking if the password dict has some entry already.
        if initial_values is not None:
            for key, value in initial_values.items():
                self.add_password(key, value)
    
    def load_password_file(self, path):
        """Loading password file"""
        
        # Giving the path to the attribute.
        self.password_file = path 
        
        # Opening file and doing stuff...
        with open(path, 'r') as f:
            for line in f:
                
                # Getting site on left and after : getting encrypted password.
                site, encrypted = line.split(':')
                
                # Assigning to site entry the value password but decrypted.
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
                
    def add_password(self, site , password):
        """Function to add password."""
        
        # Adding to the dict site and passwords not encrypted.
        self.password_dict[site] = password
        
        # If the password file is provided: 
        if self.password_file is not None:\
            # Opening the file,
            with open(self.password_file, 'a+') as f:
                
                # Generating encrypted password,
                encrypted = Fernet(self.key).encrypt(password.encode())
                
                # Writing on the file the crypted password and site on file.
                f.write(site + ':' + encrypted.decode() + '\n')
                
    def get_password(self, site):
        """Getting the password."""
        return self.password_dict[site]


def main():
    password = {
        'email':'1234567',
        'facebook':'myfbpassword'
    }
    
    pm = PasswordManager()
    
    print("""
        What do you want to do?
        1. Create new key
        2. Load existing key
        3. Create new password file
        4. Load existing password file
        5. Add new password
        6. Get password
        q. Quit
        """)   
                        
    done = False
    
    while not done:
        choice = input("Enter your choice: ") 
        if choice == '1':
            path = input('Enter path: ')
            pm.create_key(path)
            print('New key created.')
        elif choice == '2':
            path = input('Enter path: ')
            pm.load_key(path)
            print('Key successfully loaded.')
        elif choice == '3':
            path = input('Enter path: ')
            pm.create_password_file(path, password)
            print('New password file created.')
        elif choice == '4':
            path = input('Enter path: ')
            pm.load_password_file(path)
            print('Password file successfully loaded.')
        elif choice == '5':
            site = input('Enter the site: ')
            password = input('Enter the password: ')
            pm.add_password(site, password)
            print('Password added.')
        elif choice == '6':
            site = input("Enter the site: ")
            print(f"Password for {site} is: '{pm.get_password(site)}'. ")
        elif choice == 'q':
             done = True
             print('Bye')
        else:
            print('Please provide a valid entry. ')

if __name__ == "__main__":
    main()

