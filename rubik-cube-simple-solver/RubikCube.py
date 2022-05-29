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
    BLACK = 7


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
        def emoji(color):
            emoji_map = {
                Color.RED:    '🟥',
                Color.ORANGE: '🟧',
                Color.YELLOW: '🟨',
                Color.WHITE:  '⬜',
                Color.BLUE:   '🟦',
                Color.GREEN:  '🟩',
                Color.BLACK:  '⬛'
            }

            return emoji_map[color]

        pad = emoji(Color.BLACK)
        n = self.size

        for row in range(n):
            upper_lines = (pad + " ") * n \
                          + " ".join([emoji(i) for i in self.faceUp[row]]) + " " \
                          + (pad + " ") * 2 * n
            print(upper_lines)

        for row in range(n):
            middle_lines = " ".join([emoji(i) for i in self.faceLeft[row]]) + " " \
                           + " ".join([emoji(i) for i in self.faceFront[row]]) + " " \
                           + " ".join([emoji(i) for i in self.faceRight[row]]) + " " \
                           + " ".join([emoji(i) for i in self.faceBack[row]]) + " "
            print(middle_lines)

        for row in range(n):
            lower_lines = (pad + " ") * n \
                          + " ".join([emoji(i) for i in self.faceDown[row]]) + " " \
                          + (pad + " ") * 2 * n
            print(lower_lines)

    def is_solved(self) -> bool:
        """Overrides RubikCubeInterface.is_solved()"""
        return len(set([s for row in self.faceFront for s in row])) == 1 \
               and len(set([s for row in self.faceBack for s in row])) == 1 \
               and len(set([s for row in self.faceUp for s in row])) == 1 \
               and len(set([s for row in self.faceDown for s in row])) == 1 \
               and len(set([s for row in self.faceLeft for s in row])) == 1 \
               and len(set([s for row in self.faceRight for s in row])) == 1

    def __create_face(self, color):
        return [[color] * self.size] * self.size
