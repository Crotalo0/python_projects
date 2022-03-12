def main():
    print(power(3,2))

def power(n,x):
    """n elevato alla x"""
    if x == 0 and n == 0:
        return None
    if x == 0 or n == 1:
        return 1
    if n == 0:
        return 0
    if x == 1 :
        return n
    return n * power(n,x-1)
    
    


if __name__ == "__main__":
    main()