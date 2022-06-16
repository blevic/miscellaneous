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
    R_INSERT = 'RURpUpFpUpF'
    L_INSERT = 'FpUpFURURp'

    second_layer_moves = ''

    green_red_map = {
        'UF': 'U2' + L_INSERT,
        'UR': 'Up' + L_INSERT,
        'UB': L_INSERT,
        'UL': 'U' + L_INSERT,
        'FU': 'U' + R_INSERT,
        'RU': 'U2' + R_INSERT,
        'BU': 'Up' + R_INSERT,
        'LU': R_INSERT,
        'FR': '',
        'RF': R_INSERT,
        'RB': 'y' + R_INSERT + 'yp',
        'BR': 'y' + R_INSERT + 'yp',
        'BL': 'y2' + R_INSERT + 'y2',
        'LB': 'y2' + R_INSERT + 'y2',
        'LF': 'yp' + R_INSERT + 'y',
        'FL': 'yp' + R_INSERT + 'y'
    }

    for _ in range(2):
        position = cube.find([Color.GREEN, Color.RED])
        moves = green_red_map[position]
        cube.move(moves)
        second_layer_moves += moves

    red_blue_map = {
        'UF': 'yU' + L_INSERT + 'yp',
        'UR': 'yU2' + L_INSERT + 'yp',
        'UB': 'yUp' + L_INSERT + 'yp',
        'UL': 'y' + L_INSERT + 'yp',
        'FU': 'y' + R_INSERT + 'yp',
        'RU': 'yU' + R_INSERT + 'yp',
        'BU': 'yU2' + R_INSERT + 'yp',
        'LU': 'yUp' + R_INSERT + 'yp',
        'RB': '',
        'BR': 'y' + R_INSERT + 'yp',
        'BL': 'y2' + R_INSERT + 'y2',
        'LB': 'y2' + R_INSERT + 'y2',
        'LF': 'yp' + R_INSERT + 'y',
        'FL': 'yp' + R_INSERT + 'y'
    }

    for _ in range(2):
        position = cube.find([Color.RED, Color.BLUE])
        moves = red_blue_map[position]
        cube.move(moves)
        second_layer_moves += moves

    blue_orange_map = {
        'UF': 'y2' + L_INSERT + 'y2',
        'UR': 'y2U' + L_INSERT + 'y2',
        'UB': 'y2U2' + L_INSERT + 'y2',
        'UL': 'y2Up' + L_INSERT + 'y2',
        'FU': 'y2Up' + R_INSERT + 'y2',
        'RU': 'y2' + R_INSERT + 'y2',
        'BU': 'y2U' + R_INSERT + 'y2',
        'LU': 'y2U2' + R_INSERT + 'y2',
        'BL': '',
        'LB': 'y2' + R_INSERT + 'y2',
        'LF': 'yp' + R_INSERT + 'y',
        'FL': 'yp' + R_INSERT + 'y'
    }

    for _ in range(2):
        position = cube.find([Color.BLUE, Color.ORANGE])
        moves = blue_orange_map[position]
        cube.move(moves)
        second_layer_moves += moves

    orange_green_map = {
        'UF': 'ypUp' + L_INSERT + 'y',
        'UR': 'yp' + L_INSERT + 'y',
        'UB': 'ypU' + L_INSERT + 'y',
        'UL': 'ypU2' + L_INSERT + 'y',
        'FU': 'ypU2' + R_INSERT + 'y',
        'RU': 'ypUp' + R_INSERT + 'y',
        'BU': 'yp' + R_INSERT + 'y',
        'LU': 'ypU' + R_INSERT + 'y',
        'LF': '',
        'FL': 'yp' + R_INSERT + 'y'
    }

    for _ in range(2):
        position = cube.find([Color.ORANGE, Color.GREEN])
        moves = orange_green_map[position]
        cube.move(moves)
        second_layer_moves += moves

    return second_layer_moves


def top_layer(cube: RubikCubeInterface) -> str:
    def top_cross(cube: RubikCubeInterface) -> str:
        top_cross_moves = ''
        F_SWITCH = 'FRURpUpFp'

        def top_cross_done(c):
            return c.get('U') == c.get('12') == c.get('14') == c.get('16') == c.get('18')

        def just_top(c):
            return c.get('U') == c.get('02') == c.get('22') == c.get('42') == c.get('52')

        def horizontal_line(c):
            return not top_cross_done(c) and (c.get('12') == c.get('18') or c.get('14') == c.get('16'))

        def l_shape(c):
            return not top_cross_done(c) and not just_top(c) and not horizontal_line(c)

        while True:
            if top_cross_done(cube):
                return top_cross_moves

            if just_top(cube):
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if l_shape(cube):
                while cube.get('12') != cube.get('14'):
                    cube.move('U')
                    top_cross_moves += 'U'
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if horizontal_line(cube):
                if cube.get('12') == cube.get('18'):
                    cube.move('U')
                    top_cross_moves += 'U'
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

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
