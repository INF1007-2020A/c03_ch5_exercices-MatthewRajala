#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute() -> float:
    nombre = float(input('Veuillez entrer un nombre: '))

    if nombre >= 0:
        return nombre
    else:
        return nombre*-1


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'

    i = 0
    chaine_noms = []

    while i < len(prefixes): # jusqu'au dernier caractere
        chaine_noms.append(prefixes[i] + suffixes)
        i+=1

    return chaine_noms

def prime_integer_summation() -> int:
    cpt_cent = 0
    nombre = 2
    somme_des_cent_premiers = 0
    nombre_est_premier = False

    while cpt_cent < 99:
        for i in range(2, nombre):
            if (nombre % i) == 0: # si ce n'est pas un nombre premier
                nombre_est_premier = False
                break
            else: # si c'est un nombre premier
                nombre_est_premier = True

        if nombre_est_premier:
            cpt_cent += 1
            somme_des_cent_premiers += nombre

        nombre += 1

    return somme_des_cent_premiers + 2


def factorial(number: int) -> int:
    factorielle = 1

    for i in range(1, number+1):
        factorielle = factorielle*i
    return factorielle


def use_continue() -> None:
    i = 1

    while i <= 10:
        if i == 5:  # ne pas afficher 5
            i += 1
            continue
        print(i, " ", end="")
        i+=1


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
