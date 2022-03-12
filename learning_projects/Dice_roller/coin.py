#Progetto4.1
#Osservare la distribuzione di probabilita' binomiale con lancio di monete.

from tartaglia import tartagliaPyramid 

def intPrompt(prompt):
    """
    Creo un sistema di input che accetta solo int.
    In caso non sia un int ritorna il prompt.
    """
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print('Invalid entry, please provide an integer.')
            #Return to the start of the loop
        else:
            #number is integer, so we proceed into the loop.
            break
    return value

def distrib(n,k,p):
    """
    La parte che moltiplica il coefficiente binomiale nella probabilita' binomiale.
    Per il lacio della moneta, l'inverso del return di questa funzione coincide con
    il return della funzione totalDistinctCases.
    """
    distribution = ((p**k) *((1-p)**(n-k)))
    return distribution

def coinDistribution(n):
    """Stampa una determinata riga della piramide di Tartaglia"""
    x = tartagliaPyramid(n+1)[n]
    return x

def totalDistinctCases(n):
    """Somma la riga della piramide di Tartaglia per ottenere i casi possibili"""
    return sum(coinDistribution(n))

def coinProb(n):
    """Prendo ogni valore di una riga di Tartaglia e lo divido per i casi possibili."""
    row =[]
    for number in range(len(coinDistribution(n))):
        new = (coinDistribution(n)[number])/(totalDistinctCases(n))
        row.append(new)
    return row

def headsProb(heads,tosses):
    """
    Prendo le probabilita' di ogni singolo caso da coinProb. 
    Raccolgo quella specifica a quante teste voglio.
    """
    x = coinProb(tosses)
    return x[heads] 

def main():
    """Applico le funzioni per ottenere la prob di avere x teste in y lanci.""" 
    toss,head = intPrompt('Total consecutives tosses: '), intPrompt('how many heads: ')
    print(f"Possible outcomes: {totalDistinctCases(toss)} different configurations.")
    prob = (headsProb(head,toss))
    print(f"Probability of getting {head} heads in {toss} coin tosses is : {prob*100}%.")
   
if __name__ == '__main__':
    main()
