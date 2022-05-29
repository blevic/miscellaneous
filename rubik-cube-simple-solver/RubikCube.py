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
                Color.RED: '🟥',
                Color.ORANGE: '🟧',
                Color.YELLOW: '🟨',
                Color.WHITE: '⬜',
                Color.BLUE: '🟦',
                Color.GREEN: '🟩',
                Color.BLACK: '⬛'
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

    def move(self, turn: str) -> None:
        """Overrides RubikCubeInterface.move(turn)"""
        turn_functions = {
            'F': self.__move_F,
            'B': self.__move_B,
            'U': self.__move_U,
            'D': self.__move_D,
            'L': self.__move_L,
            'R': self.__move_R,
            'f': self.__move_f,
            'b': self.__move_b,
            'u': self.__move_u,
            'd': self.__move_d,
            'l': self.__move_l,
            'r': self.__move_r,
            'x': self.__move_x,
            'y': self.__move_y,
            'z': self.__move_z,
            'M': self.__move_M,
            'E': self.__move_E,
            'S': self.__move_S
        }

        turn_functions[turn]()

    @staticmethod
    def __rotate_clockwise(face: list) -> list:
        return [[face[j][i] for j in range(len(face[0]) - 1, -1, -1)] for i in range(len(face))]

    @staticmethod
    def __rotate_counterclockwise(face: list) -> list:
        return [[face[j][i] for j in range(len(face))] for i in range(len(face[0]) - 1, -1, -1)]

    def __move_F(self) -> None:
        self.faceFront = self.__rotate_clockwise(self.faceFront)

        n = self.size

        _saved_up = self.faceUp[n - 1]
        _saved_down = self.faceDown[0]
        _saved_left = [self.faceLeft[row][n - 1] for row in range(n)]
        _saved_right = [self.faceRight[row][0] for row in range(n)]

        self.faceUp[n - 1] = _saved_left[::-1]
        self.faceDown[0] = _saved_right[::-1]

        for i in range(n):
            self.faceLeft[i][n - 1] = _saved_down[i]

        for i in range(n):
            self.faceRight[i][0] = _saved_up[i]

    def __move_B(self) -> None:
        pass

    def __move_U(self) -> None:
        pass

    def __move_D(self) -> None:
        pass

    def __move_L(self) -> None:
        pass

    def __move_R(self) -> None:
        pass

    def __move_f(self) -> None:
        pass

    def __move_b(self) -> None:
        pass

    def __move_u(self) -> None:
        pass

    def __move_d(self) -> None:
        pass

    def __move_l(self) -> None:
        pass

    def __move_r(self) -> None:
        pass

    def __move_x(self) -> None:
        pass

    def __move_y(self) -> None:
        pass

    def __move_z(self) -> None:
        pass

    def __move_M(self) -> None:
        pass

    def __move_E(self) -> None:
        pass

    def __move_S(self) -> None:
        pass

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
