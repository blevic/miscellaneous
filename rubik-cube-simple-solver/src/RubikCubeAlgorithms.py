from Color import Color
from RubikCubeInterface import RubikCubeInterface


def initial_rotation(cube: RubikCubeInterface) -> list:
    """Make cube rotations to set initial standard position"""

    moves_list = []

    def green_to_front():
        green_to_front_map = {
            'F': [],
            'B': ['x2'],
            'U': ['xp'],
            'D': ['x'],
            'R': ['y'],
            'L': ['yp']
        }

        green_face = cube.find([Color.GREEN])
        moves = green_to_front_map[green_face]
        cube.move(''.join(moves))
        return moves

    def white_to_up():
        white_to_up_map = {
            'U': [],
            'D': ['z2'],
            'R': ['zp'],
            'L': ['z']
        }

        white_face = cube.find([Color.WHITE])
        moves = white_to_up_map[white_face]
        cube.move(''.join(moves))
        return moves

    moves_list += green_to_front()
    moves_list += white_to_up()

    return moves_list


def base_layer(cube: RubikCubeInterface) -> list:
    moves = []

    def base_cross(cube: RubikCubeInterface) -> list:
        return []

    def base_corners(cube: RubikCubeInterface) -> list:
        return []

    moves += base_cross(cube)
    moves += base_corners(cube)

    return moves


def second_layer(cube: RubikCubeInterface) -> list:
    moves = []

    def edges(cube: RubikCubeInterface) -> list:
        return []

    moves += edges(cube)

    return moves


def top_layer(cube: RubikCubeInterface) -> list:
    moves = []

    def top_cross(cube: RubikCubeInterface) -> list:
        return []

    def cross_color_matching(cube: RubikCubeInterface) -> list:
        return []

    def corner_matching(cube: RubikCubeInterface) -> list:
        return []

    def final_round(cube: RubikCubeInterface) -> list:
        return []

    moves += top_cross(cube)
    moves += cross_color_matching(cube)
    moves += corner_matching(cube)
    moves += final_round(cube)

    return moves


def layer_by_layer(cube: RubikCubeInterface) -> str:
    if cube.is_solved():
        return ''

    if cube.size != 3:
        raise ValueError('LBL algorithm is valid for cube size 3 only.')

    moves = initial_rotation(cube)
    moves += base_layer(cube)
    moves += second_layer(cube)
    moves += top_layer(cube)

    return " ".join(moves)
