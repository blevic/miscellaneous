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

    def move(self, turns: str) -> None:
        """Overrides RubikCubeInterface.move(turns)"""
        allowed_moves = set("FBUDLRfbudlrxyzMES")
        allowed_modifiers = set("2p′")

        move_base_functions = {
            'F': self.__move_F,
            'x': self.__move_x,
            'y': self.__move_y
        }

        move_equivalence = {
            "B": "x2Fx2",
            "U": "x′Fx",
            "D": "xFx′",
            "L": "y′Fy",
            "R": "yFy′",
            "f": "zB",
            "b": "z′F",
            "u": "yD",
            "d": "y′U",
            "l": "x′R",
            "r": "xL",
            "z": "xyx′",
            "M": "lL′",
            "E": "dD′",
            "S": "fF′"
        }

        def parse_sequence(s):
            if len(s) <= 2:
                if len(s) == 0:
                    return []
                elif len(s) == 1:
                    if s in allowed_moves:
                        return [s]
                    else:
                        raise ValueError("Unrecognized move was requested: '" + s + "'")
                elif len(s) == 2:
                    if s[0] in allowed_moves and s[1] in allowed_moves:
                        return [s[0], s[1]]
                    elif s[0] in allowed_moves and s[1] in allowed_modifiers:
                        return [s]
                    else:
                        raise ValueError("Unrecognized move(s) requested: '" + s + "'")
            else:
                if s[0] in allowed_moves and s[1] in allowed_modifiers:
                    return [s[:2]] + parse_sequence(s[2:])
                elif s[0] in allowed_moves:
                    return [s[:1]] + parse_sequence(s[1:])
                else:
                    raise ValueError("Unrecognized move was requested: '" + s[0] + "'")

        for move in parse_sequence(turns):
            if len(move) == 1:
                if move in move_base_functions:
                    move_base_functions[move]()
                elif move in move_equivalence:
                    self.move(move_equivalence[move])
                else:
                    raise ValueError("Unrecognized move: " + move)

            elif len(move) == 2:
                if move[1] in 'p′':
                    for _ in range(3):
                        self.move(move[0])
                elif move[1] == '2':
                    for _ in range(2):
                        self.move(move[0])
                else:
                    raise ValueError("Unrecognized modifier. Move: " + move)
            else:
                raise ValueError("Unrecognized move length. Move: " + move)

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

    def __move_x(self) -> None:
        self.faceRight = self.__rotate_clockwise(self.faceRight)
        self.faceLeft = self.__rotate_counterclockwise(self.faceLeft)

        _saved_up = self.faceUp
        _saved_down = self.faceDown
        _saved_front = self.faceFront
        _saved_back = self.faceBack

        self.faceUp = _saved_front
        self.faceDown = [i[::-1] for i in _saved_back[::-1]]
        self.faceFront = _saved_down
        self.faceBack = [i[::-1] for i in _saved_up[::-1]]

    def __move_y(self) -> None:
        self.faceUp = self.__rotate_clockwise(self.faceUp)
        self.faceDown = self.__rotate_counterclockwise(self.faceDown)

        _saved_front = self.faceFront
        _saved_back = self.faceBack
        _saved_left = self.faceLeft
        _saved_right = self.faceRight

        self.faceFront = _saved_right
        self.faceBack = _saved_left
        self.faceLeft = _saved_front
        self.faceRight = _saved_back

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
