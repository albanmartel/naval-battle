#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
from Positions import Positions

@dataclass
class Boat():
    boats: ClassVar[list[Boat]] = []

    @classmethod
    def nb_boats(cls):
        return len(cls.boats())


    def __init__(self, type, startposition, endposition, gameover):
        positions = Positions(startposition, endposition)
        self.type = type
        self.startposition = startposition
        self.endposition = endposition
        self.originals_squares = positions.terminate_squares()
        self.left_squares = positions.terminate_squares()
        Boat.boats.append(self)

