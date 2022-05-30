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
            'S': self.__move_S,
            'Fp': self.__move_Fp,
            'Bp': self.__move_Bp,
            'Up': self.__move_Up,
            'Dp': self.__move_Dp,
            'Lp': self.__move_Lp,
            'Rp': self.__move_Rp,
            'fp': self.__move_fp,
            'bp': self.__move_bp,
            'up': self.__move_up,
            'dp': self.__move_dp,
            'lp': self.__move_lp,
            'rp': self.__move_rp,
            'xp': self.__move_xp,
            'yp': self.__move_yp,
            'zp': self.__move_zp,
            'Mp': self.__move_Mp,
            'Ep': self.__move_Ep,
            'Sp': self.__move_Sp,
            'F′': self.__move_Fp,
            'B′': self.__move_Bp,
            'U′': self.__move_Up,
            'D′': self.__move_Dp,
            'L′': self.__move_Lp,
            'R′': self.__move_Rp,
            'f′': self.__move_fp,
            'b′': self.__move_bp,
            'u′': self.__move_up,
            'd′': self.__move_dp,
            'l′': self.__move_lp,
            'r′': self.__move_rp,
            'x′': self.__move_xp,
            'y′': self.__move_yp,
            'z′': self.__move_zp,
            'M′': self.__move_Mp,
            'E′': self.__move_Ep,
            'S′': self.__move_Sp,
            'F2': self.__move_F2,
            'B2': self.__move_B2,
            'U2': self.__move_U2,
            'D2': self.__move_D2,
            'L2': self.__move_L2,
            'R2': self.__move_R2,
            'f2': self.__move_f2,
            'b2': self.__move_b2,
            'u2': self.__move_u2,
            'd2': self.__move_d2,
            'l2': self.__move_l2,
            'r2': self.__move_r2,
            'x2': self.__move_x2,
            'y2': self.__move_y2,
            'z2': self.__move_z2,
            'M2': self.__move_M2,
            'E2': self.__move_E2,
            'S2': self.__move_S2
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
            turn_functions[move]()

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
        self.move("x2Fx2")

    def __move_U(self) -> None:
        self.move("x′Fx")

    def __move_D(self) -> None:
        self.move("xFx′")

    def __move_L(self) -> None:
        self.move("y′Fy")

    def __move_R(self) -> None:
        self.move("yFy′")

    def __move_f(self) -> None:
        self.move("zB")

    def __move_b(self) -> None:
        self.move("z′F")

    def __move_u(self) -> None:
        self.move("yD")

    def __move_d(self) -> None:
        self.move("y′U")

    def __move_l(self) -> None:
        self.move("x′R")

    def __move_r(self) -> None:
        self.move("xL")

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

    def __move_z(self) -> None:
        self.move("xyx′")

    def __move_M(self) -> None:
        self.move("lL′")

    def __move_E(self) -> None:
        self.move("dD′")

    def __move_S(self) -> None:
        self.move("fF′")

    def __move_Fp(self) -> None:
        self.move("FFF")

    def __move_Bp(self) -> None:
        self.move("BBB")

    def __move_Up(self) -> None:
        self.move("UUU")

    def __move_Dp(self) -> None:
        self.move("DDD")

    def __move_Lp(self) -> None:
        self.move("LLL")

    def __move_Rp(self) -> None:
        self.move("RRR")

    def __move_fp(self) -> None:
        self.move("fff")

    def __move_bp(self) -> None:
        self.move("bbb")

    def __move_up(self) -> None:
        self.move("uuu")

    def __move_dp(self) -> None:
        self.move("ddd")

    def __move_lp(self) -> None:
        self.move("lll")

    def __move_rp(self) -> None:
        self.move("rrr")

    def __move_xp(self) -> None:
        self.move("xxx")

    def __move_yp(self) -> None:
        self.move("yyy")

    def __move_zp(self) -> None:
        self.move("zzz")

    def __move_Mp(self) -> None:
        self.move("MMM")

    def __move_Ep(self) -> None:
        self.move("EEE")

    def __move_Sp(self) -> None:
        self.move("SSS")

    def __move_F2(self) -> None:
        self.move("FF")

    def __move_B2(self) -> None:
        self.move("BB")

    def __move_U2(self) -> None:
        self.move("UU")

    def __move_D2(self) -> None:
        self.move("DD")

    def __move_L2(self) -> None:
        self.move("LL")

    def __move_R2(self) -> None:
        self.move("RR")

    def __move_f2(self) -> None:
        self.move("ff")

    def __move_b2(self) -> None:
        self.move("bb")

    def __move_u2(self) -> None:
        self.move("uu")

    def __move_d2(self) -> None:
        self.move("dd")

    def __move_l2(self) -> None:
        self.move("ll")

    def __move_r2(self) -> None:
        self.move("rr")

    def __move_x2(self) -> None:
        self.move("xx")

    def __move_y2(self) -> None:
        self.move("yy")

    def __move_z2(self) -> None:
        self.move("zz")

    def __move_M2(self) -> None:
        self.move("MM")

    def __move_E2(self) -> None:
        self.move("EE")

    def __move_S2(self) -> None:
        self.move("SS")

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
