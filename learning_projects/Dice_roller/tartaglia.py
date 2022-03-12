#Piramide di Tartaglia
#Utile per il calcolo del coefficiente binomiale
from math import factorial

def  binomialCoeff(n,k):
    """Definizione del coefficiente binomiale."""
    coeff = ((factorial(n))/((factorial(k))*(factorial(n-k))))
    return int(coeff)

def tartagliaPyramid(rows):
    """Creo la piramide di Tartaglia."""
    result =[]
    for count in range(rows):
        row = []
        for element in range(count+1):
            row.append(binomialCoeff(count,element))
        result.append(row)
    return result

def main():
    print(tartagliaPyramid(10)[10-1])
    for row in tartagliaPyramid(3):
        print(row)

if __name__ == '__main__':
    main()   