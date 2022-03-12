def main():
    lista=[]
    for i in range(1,35):
        lista.append(fibonacci_iter(i))
    print(lista)

def fibonacci_iter(n):
    a,b=0,1
    if n == 1:
        return 0
    elif n == 2 :
        return 1
    while n-2!=0:
        c = a+b
        a = b
        b = c
        n=n-1
    return c


if __name__ == "__main__":
    main()