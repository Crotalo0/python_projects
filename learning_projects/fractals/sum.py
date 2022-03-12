def main():
    # lista1 = [1,4,5,7,32,2,1,2,465]
    # print(sumList(lista1))

    # lista2 = [1, 2, [3,4],[5,6]]
    # print(recursive_list_sum(lista2))

    num = 45
    print(integerSum(num))

def sumList(ls):
    if not ls: return  0
    return ls[0] + sumList(ls[1:])

def recursive_list_sum(ls):
    total = 0
    for element in ls:
        if type(element) is type([]):
            total = total + sumList(element)
        else:
            total = total + element
    return total

def integerSum(n):
    if n<=9:
        return n
    return int(str(n)[0]) + integerSum(int(str(n)[1:]))
    
if __name__ == "__main__":
    main()