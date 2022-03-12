def main():
    while True:
        try:
            x = int(input('Fibonacci series until term n (insert 0 to quit): '))
            if x == 0:
                break
            else:
                fib_list = [0]
                for number in range(1,x):
                    fib_list.append(fibonacci(number))

                print(f'Fibonacci series ({x} terms): \n {fib_list}')
        except ValueError:
            print('Please provide an integer.')

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
if __name__ == "__main__":
    main()