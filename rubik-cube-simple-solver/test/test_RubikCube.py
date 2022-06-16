import unittest

from Color import Color
from RubikCube import RubikCube


class TestRubikCube(unittest.TestCase):

    def test_valid_moves(self):
        valid_moves = ["F′", "", "FFF", "FpF′", "x2l2lll′", "FBUDLRLLpL′L2fulxMMEyzSS′S2"]
        cube = RubikCube()

        for moves in valid_moves:
            try:
                cube.move(moves)
            except ValueError:
                self.fail("move() raised ValueError unexpectedly!")

    def test_invalid_moves(self):
        invalid_moves = ["F'", "A", "m", "Fpp", "pF", "S22", "S3" "FfuUY", "F ", "F2′"]
        cube = RubikCube()

        for moves in invalid_moves:
            with self.assertRaises(ValueError):
                cube.move(moves)

    def test_is_solved(self):
        cube = RubikCube()
        self.assertTrue(cube.is_solved())

        cube = RubikCube()
        cube.move("xyzxpypzpx2xy2z2")
        self.assertTrue(cube.is_solved())

        cube = RubikCube()
        for i in range(6):
            cube.move("RURpUp")
            if i == 5:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        cube = RubikCube()
        for i in range(1260):
            cube.move("DRpU2M")
            if i == 1259:
                self.assertTrue(cube.is_solved())
            else:
                self.assertFalse(cube.is_solved())

        cube = RubikCube()
        cube.move("FFpBBpUUpDDpLLpRRpffpbbpuupddpllprrpxxpyypzzpMMpEEpSSp")
        self.assertTrue(cube.is_solved())

    def test_get(self):
        cube = RubikCube()
        self.assertEqual(cube.get('F'), Color.GREEN)
        self.assertEqual(cube.get('U'), Color.WHITE)
        self.assertEqual(cube.get('D'), Color.YELLOW)

        self.assertEqual(cube.get('01'), Color.GREEN)
        self.assertEqual(cube.get('11'), Color.WHITE)
        self.assertEqual(cube.get('31'), Color.YELLOW)

        cube.move("F")
        self.assertEqual(cube.get('32'), Color.RED)

        cube = RubikCube()
        for invalid_piece in ['', 'FF', 'FUY', 'Y', 'f', 'FURB', 'FB', 'UR', '15', '5', '6', '66']:
            with self.assertRaises(ValueError):
                cube.get(invalid_piece)

    def test_find(self):

        cube = RubikCube()
        self.assertEqual(cube.find([Color.GREEN]), 'F')
        self.assertEqual(cube.find([Color.WHITE]), 'U')
        self.assertEqual(cube.find([Color.RED]), 'R')

        self.assertEqual(cube.find([Color.GREEN, Color.WHITE]), 'FU')
        self.assertEqual(cube.find([Color.WHITE, Color.GREEN]), 'UF')
        self.assertEqual(cube.find([Color.GREEN, Color.RED]), 'FR')
        self.assertEqual(cube.find([Color.RED, Color.GREEN]), 'RF')

        self.assertEqual(cube.find([Color.GREEN, Color.WHITE, Color.RED]), 'FUR')
        self.assertEqual(cube.find([Color.GREEN, Color.RED, Color.WHITE]), 'FRU')
        self.assertEqual(cube.find([Color.WHITE, Color.GREEN, Color.RED]), 'UFR')
        self.assertEqual(cube.find([Color.WHITE, Color.RED, Color.GREEN]), 'URF')
        self.assertEqual(cube.find([Color.RED, Color.GREEN, Color.WHITE]), 'RFU')
        self.assertEqual(cube.find([Color.RED, Color.WHITE, Color.GREEN]), 'RUF')

        cube = RubikCube()
        cube.move('F')
        self.assertEqual(cube.find([Color.RED, Color.GREEN]), 'DF')

        cube = RubikCube()
        invalid_pieces = [
            [],
            [Color.WHITE, Color.YELLOW],
            [0, 1],
            [Color.WHITE, Color.GREEN, Color.RED, Color.YELLOW],
            [Color],
            [[Color.WHITE]]
        ]
        
        for invalid_piece in invalid_pieces:
            with self.assertRaises(ValueError):
                cube.find(invalid_piece)

    def test_get_size(self):
        cube = RubikCube()
        self.assertEqual(cube.get_size(), 3)

    def test_solve_random_scramble(self):
        for _ in range(10):
            cube = RubikCube()
            cube.scramble()
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_solve_random_scramble_with_parameters(self):
        for _ in range(10):
            cube = RubikCube()
            cube.scramble(steps=50, wide_moves=True, slice_moves=True, cube_rotations=True)
            self.assertFalse(cube.is_solved())  # extremely unlikely
            cube.solve()
            self.assertTrue(cube.is_solved())

    def test_initial_scramble_solution_concatenation(self):
        for _ in range(10):
            cube_1 = RubikCube()
            initial_scramble = cube_1.scramble(steps=40, wide_moves=True, slice_moves=True, cube_rotations=True)
            solution = cube_1.solve()

            cube_2 = RubikCube()
            cube_2.move(initial_scramble.replace(" ", "") + solution)
            self.assertTrue(cube_2.is_solved())


if __name__ == '__main__':
    unittest.main()
