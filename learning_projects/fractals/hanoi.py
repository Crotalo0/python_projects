
def showAll():   
	print(A, B, C, '_________________', sep = '\n')
    
def hanoi(n,source,destination,auxiliary):
    if n>0:
        hanoi(n-1,source,auxiliary,destination)
        destination.append(source.pop())
        showAll()
        hanoi(n-1,auxiliary,destination,source)

if __name__ == "__main__":
    A = []
    B = []
    C = []
    disks = int(input('Number of disks: '))
    A = list(range(1,disks+1)[::-1])
    print(A,B,C,'_________________',sep='\n')
    hanoi(disks, A,B,C)
    print(f'Total moves: {(2**disks)-1}')