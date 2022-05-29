from enum import Enum

from RubikCubeInterface import RubikCubeInterface

CUBE_SIZE = 3

class Color(Enum):
    """Colors enumeration"""
    RED = 1
    ORANGE = 2
    YELLOW = 3
    WHITE = 4
    BLUE = 5
    GREEN = 6


class RubikCube(RubikCubeInterface):
    """Models Rubik's Cube"""
    def __init__(self):
        self.size = CUBE_SIZE
        self.faceFront = self.__create_face(Color.RED)
        self.faceBack = self.__create_face(Color.ORANGE)
        self.faceUp = self.__create_face(Color.YELLOW)
        self.faceDown = self.__create_face(Color.WHITE)
        self.faceLeft = self.__create_face(Color.BLUE)
        self.faceRight = self.__create_face(Color.GREEN)

    def draw(self) -> None:
        """Overrides RubikCubeInterface.draw()"""
        print(self.faceFront)
        print(self.faceBack)
        print(self.faceUp)
        print(self.faceDown)
        print(self.faceLeft)
        print(self.faceRight)


    def __create_face(self, color):
        return [[color] * self.size] * self.size