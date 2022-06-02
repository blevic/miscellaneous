from RubikCubeInterface import RubikCubeInterface


def choose_base(cube: RubikCubeInterface) -> list:
    """Make cube rotations to choose base and top layers"""
    return []

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

    moves = []

    moves += choose_base(cube)
    moves += base_layer(cube)
    moves += second_layer(cube)
    moves += top_layer(cube)

    return " ".join(moves)
