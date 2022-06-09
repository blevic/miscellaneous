class RubikCubeInterface:
    def __init__(self):
        """Rubik cube fields"""
        self.size = None
        self.face_front = None
        self.face_back = None
        self.face_up = None
        self.face_down = None
        self.face_left = None
        self.face_right = None


    def draw(self) -> None:
        """Draw the cube"""
        pass

    def move(self, turns: str) -> None:
        """
        Make a sequence of moves

            Args:
                turns: sequence of letters denoting the movements/turns to be executed, according to Singmaster notation
                    Allowed letters:
                        F: Front;  B: Back;  U: Up;  D: Down;  L: Left;  R: Right;
                        f: Front 2 layers;  b: Back 2 layers;
                        u: Up 2 layers;  d: Down 2 layers;
                        l: Left 2 layers;  r: Right 2 layers;
                        x: rotation;  y: rotation;  z: rotation;
                        M: Middle;  E: Equator;  S: Standing

                    If followed by a p or a prime symbol (′), turn it anticlockwise; otherwise, turn it clockwise.
                    If followed by a 2, execute the operation twice.

                    Examples:
                        Valid:   "F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"
                        Invalid: "F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"

            Raises:
                ValueError: Unrecognized move is requested
        """
        pass

    def scramble(self, steps: int, wide_moves: bool, slice_moves: bool, cube_rotations: bool) -> str:
        """
        Scramble the cube

            Args:
                steps: number of random moves to be executed on the cube
                wide_moves: allow moves f-b-u-d-l-r to be executed
                slice_moves: allow moves M-E-S to be executed
                cube_rotations: allow rotations x-y-z to be executed

            Return:
                Sequence of scrambles executed on the cube
        """
        pass

    def is_solved(self) -> bool:
        """Respond whether the cube is solved"""
        pass

    def solve(self) -> str:
        """Return list of steps to solve the cube"""
        pass
