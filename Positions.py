#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
import Boat

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