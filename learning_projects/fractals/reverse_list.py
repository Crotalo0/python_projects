def main():
    lista = [1]
    print(reverseList(lista))
    lista2 =[1,3,56,7898]
    print(reverseList(lista2))

def reverseList(lst):
    if len(lst) in range(0,2) :
        return lst
    else: return lst[-1:] + reverseList(lst[:-1])
        
if __name__=='__main__':
    main()