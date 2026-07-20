#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
import Boat

@dataclass
class NavalBattle():
    def __init__(self, size, boats, turn, gameover):
        self.size = size
        self.boats = boats
        self.turn = turn
        self.gameover = False
