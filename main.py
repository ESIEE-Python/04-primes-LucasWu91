"""
Fichier main.py
"""
from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    Détermine si p est un nombre premier ou non

    Args :
            p : entier positive
    Returns:
            True or False

    """
    if p<= 1 :
        return False
    #si le nombre choisi est inférieure a 1, ce n'est pas un nombre premier ;
    for i in range(2,int(sqrt(p)+1)):
        if p%i==0 :
            return False
    #Si le nombre est divisible par autre chose, ce n'est pas un nombre premier ;
    return True
    #Le nombre est premier ;
#### Fonction principale


def main():
    """
    Test différentes valeurs
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
