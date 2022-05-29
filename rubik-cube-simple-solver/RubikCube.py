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

        padding = emoji(Color.BLACK)

        for row in range(self.size):
            upper_lines = (padding + " ") * self.size
            for square in range(self.size):
                upper_lines += emoji(self.faceUp[row][square]) + " "
            upper_lines += (padding + " ") * 2 * self.size
            print(upper_lines)

        for row in range(self.size):
            middle_lines = ""
            for square in range(self.size):
                middle_lines += emoji(self.faceLeft[row][square]) + " "
            for square in range(self.size):
                middle_lines += emoji(self.faceFront[row][square]) + " "
            for square in range(self.size):
                middle_lines += emoji(self.faceRight[row][square]) + " "
            for square in range(self.size):
                middle_lines += emoji(self.faceBack[row][square]) + " "
            print(middle_lines)

        for row in range(self.size):
            lower_lines = (padding + " ") * self.size
            for square in range(self.size):
                lower_lines += emoji(self.faceDown[row][square]) + " "
            lower_lines += (padding + " ") * 2 * self.size
            print(lower_lines)

    def __create_face(self, color):
        return [[color] * self.size] * self.size
