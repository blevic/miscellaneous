from itertools import permutations
from random import choice

from Color import Color
from RubikCubeAlgorithms import layer_by_layer
from RubikCubeInterface import RubikCubeInterface

CUBE_SIZE = 3


class RubikCube(RubikCubeInterface):
    """Models Rubik's Cube"""

    def __init__(self):
        self._size = n = CUBE_SIZE
        self._faces = {'F': [[Color.GREEN] * n for _ in range(n)],
                       'B': [[Color.BLUE] * n for _ in range(n)],
                       'U': [[Color.WHITE] * n for _ in range(n)],
                       'D': [[Color.YELLOW] * n for _ in range(n)],
                       'L': [[Color.ORANGE] * n for _ in range(n)],
                       'R': [[Color.RED] * n for _ in range(n)]}

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

        n = self._size

        padding = emoji(Color.BLACK) + ' '
        pad_left = padding * n
        pad_right = padding * 2 * n

        for row in range(n):
            upper_lines = pad_left + " ".join(map(emoji, self._faces['U'][row])) + " " + pad_right
            print(upper_lines)

        for row in range(n):
            middle_lines = " ".join(map(emoji, self._faces['L'][row] + self._faces['F'][row] +
                                        self._faces['R'][row] + self._faces['B'][row]))
            print(middle_lines)

        for row in range(n):
            lower_lines = pad_left + " ".join(map(emoji, self._faces['D'][row])) + " " + pad_right
            print(lower_lines)

    def move(self, turns: str) -> None:
        """Overrides RubikCubeInterface.move(turns)"""
        allowed_moves = set("FBUDLRfbudlrxyzMES")
        allowed_modifiers = set("2p′")

        move_base_functions = {
            'F': self._move_F,
            'x': self.__move_x,
            'y': self.__move_y
        }

        move_equivalence = {
            'B': "x2Fx2",
            'U': "x′Fx",
            'D': "xFx′",
            'L': "y′Fy",
            'R': "yFy′",
            'f': "zB",
            'b': "z′F",
            'u': "yD",
            'd': "y′U",
            'l': "x′R",
            'r': "xL",
            'z': "xyx′",
            'M': "lL′",
            'E': "dD′",
            'S': "fF′"
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
                if move[1] in "p′":
                    for _ in range(3):
                        self.move(move[0])
                elif move[1] == "2":
                    for _ in range(2):
                        self.move(move[0])
                else:
                    raise ValueError("Unrecognized modifier. Move: " + move)
            else:
                raise ValueError("Unrecognized move length. Move: " + move)

    @staticmethod
    def _rotate_clockwise(face: list) -> list:
        return [[face[j][i] for j in range(len(face[0]) - 1, -1, -1)] for i in range(len(face))]

    @staticmethod
    def _rotate_counterclockwise(face: list) -> list:
        return [[face[j][i] for j in range(len(face))] for i in range(len(face[0]) - 1, -1, -1)]

    def _move_F(self) -> None:
        self._faces['F'] = self._rotate_clockwise(self._faces['F'])

        n = self._size
        _saved_up = self._faces['U'][n - 1]

        self._faces['U'][n - 1] = [self._faces['L'][row][n - 1] for row in range(n)][::-1]
        self._faces['L'] = [l[:-1] + [self._faces['D'][0][i]] for i, l in enumerate(self._faces['L'])]
        self._faces['D'][0] = [self._faces['R'][row][0] for row in range(n)][::-1]
        self._faces['R'] = [[_saved_up[i]] + l[1:] for i, l in enumerate(self._faces['R'])]

    def __move_x(self) -> None:
        self._faces['R'] = self._rotate_clockwise(self._faces['R'])
        self._faces['L'] = self._rotate_counterclockwise(self._faces['L'])

        _saved_up = self._faces['U']

        self._faces['U'] = self._faces['F']
        self._faces['F'] = self._faces['D']
        self._faces['D'] = [i[::-1] for i in self._faces['B'][::-1]]
        self._faces['B'] = [i[::-1] for i in _saved_up[::-1]]

    def __move_y(self) -> None:
        self._faces['U'] = self._rotate_clockwise(self._faces['U'])
        self._faces['D'] = self._rotate_counterclockwise(self._faces['D'])

        _saved_front = self._faces['F']

        self._faces['F'] = self._faces['R']
        self._faces['R'] = self._faces['B']
        self._faces['B'] = self._faces['L']
        self._faces['L'] = _saved_front

    def scramble(self, steps=20, wide_moves=False, slice_moves=False, cube_rotations=False) -> str:
        """Overrides RubikCubeInterface.scramble(steps)"""
        if steps < 1:
            return ""

        face_turns = ['F', 'B', 'U', 'D', 'L', 'R']
        wm_lst = ['f', 'b', 'u', 'd', 'l', 'r']
        sm_lst = ['M', 'E', 'S']
        cr_lst = ['x', 'y', 'z']
        modifiers = ['', '′', '2']

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

        def solved_face(face):
            return len(set([s for row in face for s in row])) == 1

        return all(map(solved_face, self._faces.values()))

    def get_color(self, position: str) -> str:
        map_color = {Color.GREEN: 'G', Color.RED: 'R', Color.ORANGE: 'O',
                     Color.WHITE: 'W', Color.BLUE: 'B', Color.YELLOW: 'Y'}

        if position in self._faces.keys():
            color = self._faces[position][1][1]
            return map_color[color]

        map_face = {'0': 'F', '1': 'U', '2': 'L', '3': 'D', '4': 'R', '5': 'B'}

        map_singmaster = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0),
                          '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}

        if len(position) != 2 or position[0] not in map_face.keys() or position[1] not in map_singmaster.keys():
            raise ValueError("Invalid position!")

        face_id = map_face[position[0]]
        x, y = map_singmaster[position[1]]
        color = self._faces[face_id][x][y]

        return map_color[color]

    def find_position(self, *colors: str) -> str:
        if len(colors) == 0:
            raise ValueError("Empty colors -- invalid!.")

        if len(colors) == 1:
            for face in self._faces.keys():
                if colors == (self.get_color(face),):
                    return face

            raise ValueError("Face color not found!")

        if len(colors) == 2:
            edges = {
                ('F', 'U'): ('02', '18'),
                ('F', 'D'): ('08', '32'),
                ('F', 'R'): ('06', '44'),
                ('F', 'L'): ('04', '26'),
                ('B', 'U'): ('52', '12'),
                ('B', 'D'): ('58', '38'),
                ('B', 'R'): ('54', '46'),
                ('B', 'L'): ('56', '24'),
                ('R', 'U'): ('42', '16'),
                ('U', 'L'): ('14', '22'),
                ('L', 'D'): ('28', '34'),
                ('D', 'R'): ('36', '48')
            }

            for edge_id, edge_value in edges.items():
                z_dict = dict(zip(edge_value, edge_id))
                for values in permutations(edge_value):
                    if colors == tuple(map(self.get_color, values)):
                        return ''.join(z_dict[i] for i in values)
            raise ValueError("Edge colors not found!")

        if len(colors) == 3:
            corners = {
                ('F', 'U', 'R'): ('03', '19', '41'),
                ('F', 'U', 'L'): ('01', '17', '23'),
                ('B', 'U', 'R'): ('51', '13', '43'),
                ('B', 'U', 'L'): ('53', '11', '21'),
                ('F', 'D', 'L'): ('07', '31', '29'),
                ('F', 'D', 'R'): ('09', '33', '47'),
                ('B', 'D', 'L'): ('59', '37', '27'),
                ('B', 'D', 'R'): ('57', '39', '49')
            }

            for corner_id, corner_value in corners.items():
                z_dict = dict(zip(corner_value, corner_id))
                for values in permutations(corner_value):
                    if colors == tuple(map(self.get_color, values)):
                        return ''.join(z_dict[i] for i in values)
            raise ValueError("Corner colors not found!")

        raise ValueError("Invalid colors length (>3)")

    def solve(self) -> str:
        return layer_by_layer(self)

    def get_size(self) -> int:
        return self._size

    def set_color(self, position: str, color: str) -> None:
        colors = {'G': Color.GREEN, 'R': Color.RED, 'O': Color.ORANGE,
                  'W': Color.WHITE, 'B': Color.BLUE, 'Y': Color.YELLOW}

        map_face = {'0': 'F', '1': 'U', '2': 'L', '3': 'D', '4': 'R', '5': 'B'}

        map_singmaster = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0),
                          '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}

        if color not in colors:
            raise ValueError("Invalid color!")

        if position in self._faces.keys():
            self._faces[position][1][1] = colors[color]
            return

        if len(position) != 2 or position[0] not in map_face or position[1] not in map_singmaster:
            raise ValueError("Invalid position!")

        face_id = map_face[position[0]]
        x, y = map_singmaster[position[1]]

        self._faces[face_id][x][y] = colors[color]

    def set_all_colors(self, color_dict: dict) -> None:
        if len(color_dict) != 54:
            raise ValueError("Expected 54 keys in direct_dict")

        if set(color_dict.values()) != set('GROWBY'):
            raise ValueError('Expected G-R-O-W-B-Y as colors')

        for color in set('GROWBY'):
            if list(color_dict.values()).count(color) != 9:
                raise ValueError(f"Expected 9 times the color '{color}'")

        for position, color in color_dict.items():
            self.set_color(position, color)
