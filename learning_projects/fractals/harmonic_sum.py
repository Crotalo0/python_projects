from math import log

def main():
    print(harmonic_sum(6))
    print(generalized_harmonic_sum(6,1.1))
    print(altern_harmonic_sum(6,1.1))
    print(modified_harmonic_sum(6,1.1,1.5))

def harmonic_sum(n):
    harm_partial = 1/n
    if n == 1:
        return 1
    return harm_partial + harmonic_sum(n-1)

def generalized_harmonic_sum(n,alpha):
    gen_harm_partial = (1/n)**alpha
    if n == 1:
        return 1
    return gen_harm_partial + generalized_harmonic_sum(n-1,alpha)

def altern_harmonic_sum(n,alpha):
    alt_harm_partial = ((-1)**n)*((1/n)**alpha)
    if n == 1:
        return 1
    return alt_harm_partial + altern_harmonic_sum(n-1,alpha)

def modified_harmonic_sum(n,alpha,beta):
    if n >= 2 :
        mod_harm_partial = ((1/n)**alpha)*(1/(log(n))**beta)
    if n == 2 :
        return mod_harm_partial
    else:
        return mod_harm_partial + modified_harmonic_sum(n-1,alpha,beta)


if __name__ == "__main__":
    main()