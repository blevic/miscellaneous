from random import choice

from Color import Color
from RubikCubeAlgorithms import layer_by_layer
from RubikCubeInterface import RubikCubeInterface

CUBE_SIZE = 3


class RubikCube(RubikCubeInterface):
    """Models Rubik's Cube"""

    def __init__(self):
        self.size = n = CUBE_SIZE
        self.face_front = [[Color.GREEN]*n]*n
        self.face_back = [[Color.BLUE]*n]*n
        self.face_up = [[Color.WHITE]*n]*n
        self.face_down = [[Color.YELLOW]*n]*n
        self.face_left = [[Color.ORANGE]*n]*n
        self.face_right = [[Color.RED]*n]*n

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
                          + " ".join([emoji(i) for i in self.face_up[row]]) + " " \
                          + (pad + " ") * 2 * n
            print(upper_lines)

        for row in range(n):
            middle_lines = " ".join([emoji(i) for i in self.face_left[row]]) + " " \
                           + " ".join([emoji(i) for i in self.face_front[row]]) + " " \
                           + " ".join([emoji(i) for i in self.face_right[row]]) + " " \
                           + " ".join([emoji(i) for i in self.face_back[row]]) + " "
            print(middle_lines)

        for row in range(n):
            lower_lines = (pad + " ") * n \
                          + " ".join([emoji(i) for i in self.face_down[row]]) + " " \
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
        self.face_front = self.__rotate_clockwise(self.face_front)

        n = self.size
        _saved_up = self.face_up[n - 1]

        self.face_up[n - 1] = [self.face_left[row][n - 1] for row in range(n)][::-1]
        self.face_left = [l[:-1] + [self.face_down[0][i]] for i, l in enumerate(self.face_left)]
        self.face_down[0] = [self.face_right[row][0] for row in range(n)][::-1]
        self.face_right = [[_saved_up[i]] + l[1:] for i, l in enumerate(self.face_right)]

    def __move_x(self) -> None:
        self.face_right = self.__rotate_clockwise(self.face_right)
        self.face_left = self.__rotate_counterclockwise(self.face_left)

        _saved_up = self.face_up

        self.face_up = self.face_front
        self.face_front = self.face_down
        self.face_down = [i[::-1] for i in self.face_back[::-1]]
        self.face_back = [i[::-1] for i in _saved_up[::-1]]

    def __move_y(self) -> None:
        self.face_up = self.__rotate_clockwise(self.face_up)
        self.face_down = self.__rotate_counterclockwise(self.face_down)

        _saved_front = self.face_front

        self.face_front = self.face_right
        self.face_right = self.face_back
        self.face_back = self.face_left
        self.face_left = _saved_front

    def scramble(self, steps=20, wide_moves=False, slice_moves=False, cube_rotations=False) -> str:
        """Overrides RubikCubeInterface.scramble(steps)"""
        if steps < 1:
            return ""

        face_turns = ["F", "B", "U", "D", "L", "R"]
        wm_lst = ["f", "b", "u", "d", "l", "r"]
        sm_lst = ["M", "E", "S"]
        cr_lst = ["x", "y", "z"]
        modifiers = ["", "′", "2"]

        allowed_moves = face_turns + wide_moves * wm_lst + slice_moves * sm_lst + cube_rotations * cr_lst

        def choice_avoiding(lst, avoid):
            return choice([e for e in lst if e != avoid])

        move = choice(allowed_moves) + choice(modifiers)
        self.move(move)
        sequence = [move]
        for _ in range(steps - 1):
            move = choice_avoiding(allowed_moves, sequence[-1][0]) + choice(modifiers)
            self.move(move)
            sequence.append(move)

        return ' '.join(sequence)

    def is_solved(self) -> bool:
        """Overrides RubikCubeInterface.is_solved()"""
        return len(set([s for row in self.face_front for s in row])) == 1 \
               and len(set([s for row in self.face_back for s in row])) == 1 \
               and len(set([s for row in self.face_up for s in row])) == 1 \
               and len(set([s for row in self.face_down for s in row])) == 1 \
               and len(set([s for row in self.face_left for s in row])) == 1 \
               and len(set([s for row in self.face_right for s in row])) == 1

    def get(self, position: str):
        if position == 'F':
            return self.face_front[1][1]

        if position == 'B':
            return self.face_back[1][1]

        if position == 'U':
            return self.face_up[1][1]

        if position == 'D':
            return self.face_down[1][1]

        if position == 'L':
            return self.face_left[1][1]

        if position == 'R':
            return self.face_right[1][1]

        if len(position) != 2 or position[1] not in "12346789" or position[0] not in "012345":
            raise ValueError("Invalid position!")

        map_singmaster = {
            '1': (0, 0),
            '2': (0, 1),
            '3': (0, 2),
            '4': (1, 0),
            '6': (1, 2),
            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2)
        }

        face_id = position[0]
        x, y = map_singmaster[position[1]]

        if face_id == '0':
            return self.face_front[x][y]

        if face_id == '1':
            return self.face_up[x][y]

        if face_id == '2':
            return self.face_left[x][y]

        if face_id == '3':
            return self.face_down[x][y]

        if face_id == '4':
            return self.face_right[x][y]

        if face_id == '5':
            return self.face_back[x][y]

        raise ValueError("No position reached!")

    def solve(self) -> str:
        return layer_by_layer(self)
