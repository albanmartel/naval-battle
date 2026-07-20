#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass

@dataclass
class Boat():
    def __init__(self, type, startposition, endposition, gameover):
        self.type = type
        self.startposition = startposition
        self.endposition = endposition
        self.originals_squares = []
        self.left_squares = []
        self.gameover = gameover


