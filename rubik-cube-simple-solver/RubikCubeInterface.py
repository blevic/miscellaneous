class RubikCubeInterface:
    def draw(self) -> None:
        """Draw the cube"""
        pass

    def move(self, turn: str) -> None:
        """
        Move the cube

            Args:
                turn: a letter denoting the movement/turn to be executed, according to Singmaster notation
                    Allowed letters:
                        F: Front;  B: Back;  U: Up;  D: Down;  L: Left;  R: Right;
                        f: Front 2 layers;  b: Back 2 layers;
                        u: Up 2 layers;  d: Down 2 layers;
                        l: Left 2 layers;  r: Right 2 layers;
                        x: rotation;  y: rotation;  z: rotation;
                        M: Middle;  E: Equator;  S: Standing

                    If followed by prime symbol (′), turn it anticlockwise; otherwise, turn it clockwise.
                    If followed by a 2, execute the operation twice.
        """
        pass

    def shuffle(self, steps: int) -> None:
        """Shuffle the cube"""
        pass

    def is_solved(self) -> bool:
        """Respond whether the cube is solved"""
        pass

    def solve(self) -> list:
        """Return list of steps to solve the cube"""
        pass