def main():
    new_func()

def new_func():
    while True:
        try:
            x = int(input('n for factorial (insert -1 to quit): '))
            if x == -1:
                break
            else:
                print(factorial(x))
        except ValueError:
            print('Please provide an integer.')
        

def factorial(n):
    if n < 0: return 'No negative integers.'
    if n <= 1: return 1
    else: return n * factorial(n-1)


if __name__ == "__main__":
    main()