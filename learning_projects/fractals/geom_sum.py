from power import power

def main():
    print(geom_sum(0.99,996))
    print(geom_convergence(0.99))

def geom_sum(q,n):
    if n == 0:
        return 0
    return power(q,n) + geom_sum(q,n-1)

def geom_convergence(q):
    return  1/(1-q)


if __name__ == "__main__":
    main()