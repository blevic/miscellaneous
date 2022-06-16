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
        base_moves = ''

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
        base_moves += moves

        red_map = {
            'FU': 'FRpFp',
            'FR': 'Rp',
            'FL': 'F2RpF2',
            'UF': 'UpR2',
            'RF': 'FpUpFR2',
            'LF': 'FpDF',
            'BU': 'BpR',
            'BD': 'BR',
            'BR': 'R',
            'BL': 'B2R',
            'UB': 'UR2',
            'DB': 'BDBpDp',
            'RB': 'DBpDp',
            'LB': 'DBDp',
            'RU': 'UpBpR',
            'UR': 'R2',
            'UL': 'U2R2',
            'LU': 'UpFRpFp',
            'LD': 'LpFpDF',
            'DL': 'FD2Fp',
            'DR': '',
            'RD': 'RFDFp'
        }
        piece = cube.find([Color.YELLOW, Color.RED])
        moves = red_map[piece]
        cube.move(moves)
        base_moves += moves

        blue_map = {
            'FU': 'ULpB',
            'FR': 'DpRpD',
            'FL': 'DLDp',
            'UF': 'U2B2',
            'RF': 'R2BpR2',
            'LF': 'D2FpD2',
            'BU': 'BpDpRD',
            'BD': 'BDpRD',
            'BR': 'DpRD',
            'BL': 'DLpDp',
            'UB': 'B2',
            'DB': '',
            'RB': 'Bp',
            'LB': 'B',
            'RU': 'RBpRp',
            'UR': 'UpB2',
            'UL': 'UB2',
            'LU': 'LpB',
            'LD': 'LB',
            'DL': 'LpDLDp'
        }
        piece = cube.find([Color.YELLOW, Color.BLUE])
        moves = blue_map[piece]
        cube.move(moves)
        base_moves += moves

        orange_map = {
            'FU': 'FpLF',
            'FR': 'D2RpD2',
            'FL': 'L',
            'UF': 'UL2',
            'RF': 'DFDp',
            'LF': 'DFpDp',
            'BU': 'U2FpLF',
            'BR': 'D2RD2',
            'BL': 'Lp',
            'UB': 'UpL2',
            'RB': 'DpBpD',
            'LB': 'DpBD',
            'RU': 'UFpLF',
            'UR': 'U2L2',
            'UL': 'L2',
            'LU': 'UpFpLF',
            'LD': 'LpDFpDp',
            'DL': ''
        }
        piece = cube.find([Color.YELLOW, Color.ORANGE])
        moves = orange_map[piece]
        cube.move(moves)
        base_moves += moves

        return base_moves

    def base_corners(cube: RubikCubeInterface) -> str:
        corners_moves = ''

        green_red_map = {
            'BDL': 'LU2Lp',
            'BDR': 'BUBp',
            'BLU': 'U2',
            'BRU': 'U',
            'DFL': 'FUpFpUp',
            'DFR': '',
            'FLU': 'Up',
            'FRU': ''
        }
        piece = cube.find([Color.YELLOW, Color.GREEN, Color.RED])
        sorted_piece = ''.join(sorted(piece))
        moves = green_red_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        while cube.find([Color.YELLOW, Color.GREEN, Color.RED]) != 'DFR':
            moves = 'RURpUp'
            cube.move(moves)
            corners_moves += moves

        red_blue_map = {
            'BDL': 'LULp',
            'BDR': '',
            'BLU': 'U',
            'BRU': '',
            'DFL': 'FU2Fp',
            'FLU': 'U2',
            'FRU': 'Up'
        }
        piece = cube.find([Color.YELLOW, Color.RED, Color.BLUE])
        sorted_piece = ''.join(sorted(piece))
        moves = red_blue_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        while cube.find([Color.YELLOW, Color.RED, Color.BLUE]) != 'DRB':
            moves = 'BUBpUp'
            cube.move(moves)
            corners_moves += moves

        blue_orange_map = {
            'BDL': '',
            'BLU': '',
            'BRU': 'Up',
            'DFL': 'FUFp',
            'FLU': 'U',
            'FRU': 'U2'
        }
        piece = cube.find([Color.YELLOW, Color.BLUE, Color.ORANGE])
        sorted_piece = ''.join(sorted(piece))
        moves = blue_orange_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        while cube.find([Color.YELLOW, Color.BLUE, Color.ORANGE]) != 'DBL':
            moves = 'LULpUp'
            cube.move(moves)
            corners_moves += moves

        orange_green_map = {
            'BLU': 'Up',
            'BRU': 'U2',
            'DFL': '',
            'FLU': '',
            'FRU': 'U'
        }
        piece = cube.find([Color.YELLOW, Color.ORANGE, Color.GREEN])
        sorted_piece = ''.join(sorted(piece))
        moves = orange_green_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        while cube.find([Color.YELLOW, Color.ORANGE, Color.GREEN]) != 'DLF':
            moves = 'FUFpUp'
            cube.move(moves)
            corners_moves += moves

        return corners_moves

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
