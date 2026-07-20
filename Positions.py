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


def separate_letters_digits(position: str) -> tuple:
    numbers = []
    letters = []
    for character in position:
        if character.isdigit():
            numbers.append(character)
        else:
            letters.append(character)

    return int(numbers), letters