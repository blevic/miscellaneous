from RubikCubeInterface import RubikCubeInterface


def base_layer(cube: RubikCubeInterface) -> str:
    f_color = cube.get('F')
    r_color = cube.get('R')
    b_color = cube.get('B')
    l_color = cube.get('L')
    d_color = cube.get('D')

    def base_cross(cube: RubikCubeInterface) -> str:
        base_moves = ''

        f_map = {
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
        piece = cube.find(d_color, f_color)
        moves = f_map[piece]
        cube.move(moves)
        base_moves += moves

        r_map = {
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
        piece = cube.find(d_color, r_color)
        moves = r_map[piece]
        cube.move(moves)
        base_moves += moves

        b_map = {
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
        piece = cube.find(d_color, b_color)
        moves = b_map[piece]
        cube.move(moves)
        base_moves += moves

        l_map = {
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
        piece = cube.find(d_color, l_color)
        moves = l_map[piece]
        cube.move(moves)
        base_moves += moves

        return base_moves

    def base_corners(cube: RubikCubeInterface) -> str:
        corners_moves = ''

        dfr_map = {
            'BDL': 'LU2Lp',
            'BDR': 'BUBp',
            'BLU': 'U2',
            'BRU': 'U',
            'DFL': 'FUpFpUp',
            'DFR': '',
            'FLU': 'Up',
            'FRU': ''
        }
        piece = cube.find(d_color, f_color, r_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dfr_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        for _ in range(6):
            if cube.find(d_color, f_color, r_color) == 'DFR':
                break
            moves = 'RURpUp'
            cube.move(moves)
            corners_moves += moves
        else:
            raise ValueError("Exceeded moves trying to match DFR")

        drb_map = {
            'BDL': 'LULp',
            'BDR': '',
            'BLU': 'U',
            'BRU': '',
            'DFL': 'FU2Fp',
            'FLU': 'U2',
            'FRU': 'Up'
        }
        piece = cube.find(d_color, r_color, b_color)
        sorted_piece = ''.join(sorted(piece))
        moves = drb_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        for _ in range(6):
            if cube.find(d_color, r_color, b_color) == 'DRB':
                break
            moves = 'BUBpUp'
            cube.move(moves)
            corners_moves += moves
        else:
            raise ValueError("Exceeded moves trying to match DRB")

        dbl_map = {
            'BDL': '',
            'BLU': '',
            'BRU': 'Up',
            'DFL': 'FUFp',
            'FLU': 'U',
            'FRU': 'U2'
        }
        piece = cube.find(d_color, b_color, l_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dbl_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        for _ in range(6):
            if cube.find(d_color, b_color, l_color) == 'DBL':
                break
            moves = 'LULpUp'
            cube.move(moves)
            corners_moves += moves
        else:
            raise ValueError("Exceeded moves trying to match DBL")

        dlf_map = {
            'BLU': 'Up',
            'BRU': 'U2',
            'DFL': '',
            'FLU': '',
            'FRU': 'U'
        }
        piece = cube.find(d_color, l_color, f_color)
        sorted_piece = ''.join(sorted(piece))
        moves = dlf_map[sorted_piece]
        cube.move(moves)
        corners_moves += moves

        for _ in range(6):
            if cube.find(d_color, l_color, f_color) == 'DLF':
                break
            moves = 'FUFpUp'
            cube.move(moves)
            corners_moves += moves
        else:
            raise ValueError("Exceeded moves trying to match DLF")

        return corners_moves

    moves_sequence = base_cross(cube)
    moves_sequence += base_corners(cube)

    return moves_sequence


def second_layer(cube: RubikCubeInterface) -> str:
    R_INSERT = 'RURpUpFpUpF'
    L_INSERT = 'FpUpFURURp'
    f_color = cube.get('F')
    r_color = cube.get('R')
    b_color = cube.get('B')
    l_color = cube.get('L')

    second_layer_moves = ''

    fr_map = {
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
        position = cube.find(f_color, r_color)
        moves = fr_map[position]
        cube.move(moves)
        second_layer_moves += moves

    rb_map = {
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
        position = cube.find(r_color, b_color)
        moves = rb_map[position]
        cube.move(moves)
        second_layer_moves += moves

    bl_map = {
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
        position = cube.find(b_color, l_color)
        moves = bl_map[position]
        cube.move(moves)
        second_layer_moves += moves

    lf_map = {
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
        position = cube.find(l_color, f_color)
        moves = lf_map[position]
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

        for _ in range(2):
            if top_cross_done(cube):
                return top_cross_moves

            if just_top(cube):
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if l_shape(cube):
                for i in range(4):
                    if cube.get('12') == cube.get('14'):
                        break
                    cube.move('U')
                    top_cross_moves += 'U'
                else:
                    raise ValueError("Expected l shape to be found")
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

            if horizontal_line(cube):
                if cube.get('12') == cube.get('18'):
                    cube.move('U')
                    top_cross_moves += 'U'
                cube.move(F_SWITCH)
                top_cross_moves += F_SWITCH

    def cross_color_matching(cube: RubikCubeInterface) -> str:
        cross_color_matching_moves = ''

        def f_match(c):
            return c.get('F') == c.get('02')

        def r_match(c):
            return c.get('R') == c.get('42')

        def b_match(c):
            return c.get('B') == c.get('52')

        def l_match(c):
            return c.get('L') == c.get('22')

        def count_matched(c):
            return sum([f_match(c), r_match(c), b_match(c), l_match(c)])

        def match_across(c):
            return count_matched(c) == 2 and (f_match(c) and b_match(c)) or (r_match(c) and l_match(c))

        def match_l(c):
            return count_matched(c) == 2 and not match_across(c)

        def matched_l_position(c):
            if not match_l(c):
                raise ValueError("Incorrect use of matched_l_position: no l matched")
            if f_match(c) and r_match(c):
                return "FR"
            if r_match(c) and b_match(c):
                return "RB"
            if b_match(c) and l_match(c):
                return "BL"
            if l_match(c) and f_match(c):
                return "LF"
            raise ValueError("No L match found")

        if count_matched(cube) == 4:
            return ''

        candidate_moves = ''
        for _ in range(4):
            candidate_moves += 'U'
            cube.move('U')
            if count_matched(cube) == 4:
                return candidate_moves

        CROSS_COLOR_MATCH_SEQ = 'RURpURU2Rp'

        # two colors are matchable
        for _ in range(4):
            if count_matched(cube) == 2:
                break
            cross_color_matching_moves += 'U'
            cube.move('U')
        else:
            ValueError("Expected two colors to match")

        if match_across(cube):
            cross_color_matching_moves += CROSS_COLOR_MATCH_SEQ
            cube.move(CROSS_COLOR_MATCH_SEQ)

        for _ in range(4):
            if count_matched(cube) == 2:
                break
            cross_color_matching_moves += 'U'
            cube.move('U')
        else:
            ValueError("Expected two colors to match")

        matched_l_position_map = {
            'FR': 'yp' + CROSS_COLOR_MATCH_SEQ + 'y',
            'RB': CROSS_COLOR_MATCH_SEQ,
            'BL': 'y' + CROSS_COLOR_MATCH_SEQ + 'yp',
            'LF': 'y2' + CROSS_COLOR_MATCH_SEQ + 'y2'
        }

        if not match_l(cube):
            raise ValueError("Expected L matched by here")

        moves = matched_l_position_map[matched_l_position(cube)]
        cross_color_matching_moves += moves
        cube.move(moves)

        if count_matched(cube) == 4:
            return ''

        for _ in range(4):
            cross_color_matching_moves += 'U'
            cube.move('U')
            if count_matched(cube) == 4:
                return cross_color_matching_moves

        raise ValueError("Expected top cross to be color matched by here")

    def corner_matching(cube: RubikCubeInterface) -> str:
        corner_matching_moves = ''
        SWAP_CORNERS = 'URUpLpURpUpL'

        def number_matching_corners(c):
            return sum([
                ''.join(sorted(c.find(c.get('B'), c.get('L'), c.get('U')))) == 'BLU',
                ''.join(sorted(c.find(c.get('B'), c.get('R'), c.get('U')))) == 'BRU',
                ''.join(sorted(c.find(c.get('F'), c.get('L'), c.get('U')))) == 'FLU',
                ''.join(sorted(c.find(c.get('F'), c.get('R'), c.get('U')))) == 'FRU'
            ])

        def matching_up_corner_position(c):
            if number_matching_corners(c) != 1:
                raise ValueError("Function matching_up_corner_position is valid only for 1 matching top corner")
            if ''.join(sorted(c.find(c.get('B'), c.get('L'), c.get('U')))) == 'BLU':
                return 'BL'
            if ''.join(sorted(c.find(c.get('B'), c.get('R'), c.get('U')))) == 'BRU':
                return 'BR'
            if ''.join(sorted(c.find(c.get('F'), c.get('L'), c.get('U')))) == 'FLU':
                return 'FL'
            if ''.join(sorted(c.find(c.get('F'), c.get('R'), c.get('U')))) == 'FRU':
                return 'FR'
            raise ValueError("Expected any top position to be found")

        if number_matching_corners(cube) == 4:
            return ''

        if number_matching_corners(cube) == 0:
            corner_matching_moves += SWAP_CORNERS
            cube.move(SWAP_CORNERS)

        if number_matching_corners(cube) != 1:
            raise ValueError("Expected 1 matching top corner")

        matching_up_corner = matching_up_corner_position(cube)

        rotation_map = {
            'BL': ('y2', 'y2'),
            'BR': ('y', 'yp'),
            'FL': ('yp', 'y'),
            'FR': ('', '')
        }

        pre_rotation, post_rotation = rotation_map[matching_up_corner]

        corner_matching_moves += pre_rotation
        cube.move(pre_rotation)
        for _ in range(2):
            corner_matching_moves += SWAP_CORNERS
            cube.move(SWAP_CORNERS)

            if number_matching_corners(cube) == 4:
                corner_matching_moves += post_rotation
                cube.move(post_rotation)
                return corner_matching_moves

        raise ValueError("Expected corners to be matched by here")

    def final_round(cube: RubikCubeInterface) -> str:
        final_round_moves = ''
        R_MOVES = 'RURpUp'

        if cube.is_solved():
            return ''

        final_round_moves += 'x2'
        cube.move('x2')

        for _ in range(5):
            if cube.is_solved():
                break
            for i in range(6):
                if cube.get('33') == cube.get('D'):
                    break
                final_round_moves += R_MOVES
                cube.move(R_MOVES)
            else:
                raise ValueError("Expected bottom piece to be solved")
            final_round_moves += 'D'
            cube.move('D')
        else:
            raise ValueError("Expected cube to be solved")

        return final_round_moves

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

    moves = base_layer(cube)
    moves += second_layer(cube)
    moves += top_layer(cube)

    return moves.replace("p", "′")
