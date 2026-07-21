#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
import Naval_battle

def main()-> None:
    bataille_navale = Naval_battle.Naval_battle(10)
    bateaux = bataille_navale.boats
    for bateau in bateaux:
        print(f"\"{bateau.type}\": {bateau.originals_squares}")


if __name__ == "__main__":
    print("Jeu de la bataille navale")
    main()
