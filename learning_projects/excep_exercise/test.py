#Esercizio try except.

def int_input(text: str):
    while True:
        try:
            n = int(input(text))
            if n >= 0:
                return n
            else:
                print('Integer must be positive (or zero).')

        except ValueError:
            print('Please, insert a valid integer (also cannot accept no input).')

def main():
    num = int_input('integer: ')
    print(num)

if __name__=='__main__':
    main()
    

   