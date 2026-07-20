#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
import Boat

##### Les Constantes ######
boats_coordoodinates = (
    ("B2", "B2"),
    ("A4", "A7"),
    ("C5", "C7"),
    ("H5", "J5"),
    ("E9", "F9"),
)

@dataclass
class NavalBattle():
    def __init__(self, size, boats, turn, gameover):
        self.size = size
        self.boats = boats
        self.turn = turn
        self.gameover = False
