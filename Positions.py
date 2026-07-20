#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from dataclasses import dataclass

@dataclass
class Positions():
    def __init__(self, startposition: str, endposition: str):
        self.startposition = startposition
        self.endposition = endposition


    @staticmethod
    def separate_letters_digits(position: str) -> tuple:
        """
        fonction separate_letters_digits(position: str)
        permet de séparer dans la position la partie des lettres
        de la partie des entiers.
        :param position: chaîne de caractère de la forme "A1"
        :return: un tuple de lettres et de nombre séparés
        """
        numbers = []
        letters = []
        for character in position:
            if character.isdigit():
                numbers.append(character)
            else:
                letters.append(character)

        return letters, numbers


    @staticmethod
    def determinate_squares(self) -> tuple:
        """
        fonction determinate_squares(self)
        permet d'obtenir toutes les case d'un bâteau
        :param self: l'instance elle-même
        :return: un tableau de cases de bâteau
        """
        position = self.separate_letters_digits(self.startposition)
        letters_1 = position[0]
        numbers_1 = position[1]
        position = self.separate_letters_digits(self.endposition)
        letters_2 = position[0]
        numbers_2 = position[1]

        squares = []
        if letters_1 == letters_2:
            if int(numbers_1) < int(numbers_2):
                for number in range(int(numbers_1), int(numbers_2) + 1):
                    squares.append(letters_1 + str(number))
            elif int(numbers_1) > int(numbers_2):
                for number in range(int(numbers_2), int(numbers_1) + 1):
                    squares.append(letters_1 + str(number))
        if numbers_1 == numbers_2:
            if ord(letters_1) < ord(letters_2):
                for idx in range(ord(letters_1), ord(letters_2) + 1):
                    squares.append(chr(idx) + str(number))
            elif ord(letters_1) > ord(letters_2):
                for idx in range(ord(letters_2), ord(letters_1) + 1):
                    squares.append(chr(idx) + str(number))

        return squares