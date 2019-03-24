import math
from typing import Tuple, Optional

import rlbot.utils.structures.game_data_struct as game_data_struct

from utils import *


VectorArgument = Union[float, game_data_struct.Vector3]


class Vector2:
    def __init__(self, x: VectorArgument, y: Optional[float] = None):
        self.x: float = 0
        self.y: float = 0

        if isinstance(x, game_data_struct.Vector3):
            self.x = x.x
            self.y = x.y
        elif y is not None:
            self.x = x
            self.y = y
        else:
            raise TypeError("Wrong type(s) given for Vector2.x and/or Vector2.y")

    def __add__(self, v: "Vector2") -> "Vector2":
        return Vector2(self.x + v.x, self.y + v.y)

    def __sub__(self, v: "Vector2") -> "Vector2":
        return Vector2(self.x - v.x, self.y - v.y)
    
    def __mul__(self, v: float) -> "Vector2":
        return Vector2(self.x * v, self.y * v)

    def __truediv__(self, v: float) -> "Vector2":
        return Vector2(self.x / v, self.y / v)

    def __rmul__(self, v: float) -> "Vector2":
        return Vector2(self.x * v, self.y * v)

    def __rtruediv__(self, v: float) -> "Vector2":
        return Vector2(self.x / v, self.y / v)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other: "Vector2") -> bool:
        if isinstance(other, Vector2):
            if other.x == self.y and other.y == self.y:
                return True
            return False
        return False

    def __neg__(self) -> "Vector2":
        return -1 * self
    
    def __getitem__(self, item: int) -> float:
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError("Invalid index for accessing Vector2. Must be 0 or 1.")
    
    def __setitem__(self, key: int, value: float):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Invalid index for accessing Vector2. Must be 0 or 1.")

    def correction_to(self, ideal):
        correction = math.atan2(self.y, -self.x) - math.atan2(ideal.y, -ideal.x) # The in-game axes are left handed, so use -x
        return correction if abs(correction) <= math.pi else (sign(correction) * 2 * math.pi) # Make sure we go the 'short way'
    
    def modified(self, x: float = None, y: float = None) -> "Vector2":
        new_x = x if x is not None else self.x
        new_y = y if y is not None else self.y
        return Vector2(new_x, new_y)

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def size(self) -> float:
        return self.length
    
    @property
    def as_tuple(self) -> Tuple[float]:
        return self.x, self.y


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, val):
        return Vector3(self.x + val.x, self.y + val.y, self.z + val.z)

    def __sub__(self, val):
        return Vector3(self.x - val.x, self.y - val.y, self.z - val.z)

    def flatten(self) -> Vector2:
        return Vector2(self.x, self.y)

    @property
    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @property
    def size(self) -> float:
        return self.length

class life(int):
    math = False

love = life()
assert love <3
