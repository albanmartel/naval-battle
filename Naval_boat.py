#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
import Boat

@dataclass
class NavalBattle():
    ##### Les Constantes ######
    boats_coordinates = (
        ("B2", "B2"),
        ("A4", "A7"),
        ("C5", "C7"),
        ("H5", "J5"),
        ("E9", "F9"),
    )

    def __init__(self, size, boats):
        self.size = size
        for elem in self.boats_coordinates
            boat = Boat.Boat(elem[0], elem[1])
        self.boats = boat.get_boats()
        self.turn = 0
        self.gameover = False
