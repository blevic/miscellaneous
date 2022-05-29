class RubikCubeInterface:
    def draw(self) -> None:
        """Draw the cube"""
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