from Color import Color
from RubikCubeInterface import RubikCubeInterface


def initial_rotation(cube: RubikCubeInterface) -> str:
    """Make cube rotations to set initial standard position"""

    def green_to_front():
        green_to_front_map = {
            'F': '',
            'B': 'x2',
            'U': 'xp',
            'D': 'x',
            'R': 'y',
            'L': 'yp'
        }

        green_face = cube.find([Color.GREEN])
        moves = green_to_front_map[green_face]
        cube.move(moves)
        return moves

    def white_to_up():
        white_to_up_map = {
            'U': '',
            'D': 'z2',
            'R': 'zp',
            'L': 'z'
        }

        white_face = cube.find([Color.WHITE])
        moves = white_to_up_map[white_face]
        cube.move(moves)
        return moves

    moves_sequence = green_to_front()
    moves_sequence += white_to_up()

    return moves_sequence


def base_layer(cube: RubikCubeInterface) -> str:
    def base_cross(cube: RubikCubeInterface) -> str:
        green_map = {
            'FU': 'FRpDp',
            'FD': 'FLD',
            'FR': 'RpDp',
            'FL': 'LD',
            'UF': 'F2',
            'DF': '',
            'RF': 'F',
            'LF': 'Fp',
            'BU': 'URpF',
            'BD': 'DLpFp',
            'BR': 'RDp',
            'BL': 'LpD',
            'UB': 'U2F2',
            'DB': 'D2',
            'RB': 'R2F',
            'LB': 'L2Fp',
            'RU': 'RpF',
            'UR': 'UF2',
            'UL': 'UpF2',
            'LU': 'LFp',
            'LD': 'LpFp',
            'DL': 'D',
            'DR': 'Dp',
            'RD': 'RF'
        }
        piece = cube.find([Color.YELLOW, Color.GREEN])
        moves = green_map[piece]
        cube.move(moves)

        # red
        red_map = {

        }

        # blue
        blue_map = {

        }

        # orange
        orange_map = {

        }
        return moves

    def base_corners(cube: RubikCubeInterface) -> str:
        return ''

    moves_sequence = base_cross(cube)
    moves_sequence += base_corners(cube)

    return moves_sequence


def second_layer(cube: RubikCubeInterface) -> str:
    def edges(cube: RubikCubeInterface) -> str:
        return ''

    moves = edges(cube)

    return ''


def top_layer(cube: RubikCubeInterface) -> str:
    def top_cross(cube: RubikCubeInterface) -> str:
        return ''

    def cross_color_matching(cube: RubikCubeInterface) -> str:
        return ''

    def corner_matching(cube: RubikCubeInterface) -> str:
        return ''

    def final_round(cube: RubikCubeInterface) -> str:
        return ''

    moves = top_cross(cube)
    moves += cross_color_matching(cube)
    moves += corner_matching(cube)
    moves += final_round(cube)

    return moves


def layer_by_layer(cube: RubikCubeInterface) -> str:
    if cube.is_solved():
        return ''

    if cube.get_size() != 3:
        raise ValueError('LBL algorithm is valid for cube size 3 only.')

    moves = initial_rotation(cube)
    moves += base_layer(cube)
    moves += second_layer(cube)
    moves += top_layer(cube)

    return moves
