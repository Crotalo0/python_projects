def main():
    print(int_to_str(1453,16))
    

def int_to_str(n,base):
    convert = '0123456789ABCDEF'
    if n < base:
        return convert[n]
    else:
        return int_to_str(n//base,base) + convert[n%base]

if __name__ == "__main__":
    main()
