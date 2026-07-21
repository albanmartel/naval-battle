#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
import Boat

@dataclass
class Naval_battle():
    ##### Les Constantes ######
    boats_coordinates = (
        ("aircraft carrier", "B2", "F2"),
        ("cruiser", "A4", "A7"),
        ("destroyer", "C5", "C7"),
        ("submarine", "H5", "J5"),
        ("torpedo_boat", "E9", "F9"),
    )

    def __init__(self, size):
        self.size = size
        all_boats = []
        for elem in self.boats_coordinates:
            boat = Boat.Boat(elem[0], elem[1], elem[2], False)
            all_boats.append(boat)

        self.boats = all_boats
        self.turn = 0
        self.gameover = False

    # --- GETTER ---
    @property
    def boats(self):
        return self._boats

    @boats.setter
    def boats(self, boats):
        self._boats = boats