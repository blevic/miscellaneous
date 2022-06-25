import unittest

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

    def test_get_color(self):
        cube = RubikCube()
        self.assertEqual(cube.get_color('F'), 'G')
        self.assertEqual(cube.get_color('U'), 'W')
        self.assertEqual(cube.get_color('D'), 'Y')

        self.assertEqual(cube.get_color('01'), 'G')
        self.assertEqual(cube.get_color('11'), 'W')
        self.assertEqual(cube.get_color('31'), 'Y')

        cube.move("F")
        self.assertEqual(cube.get_color('32'), 'R')

        cube = RubikCube()
        for invalid_piece in ['', 'FF', 'FUY', 'Y', 'f', 'FURB', 'FB', 'UR', '15', '5', '6', '66']:
            with self.assertRaises(ValueError):
                cube.get_color(invalid_piece)

    def test_find_position(self):

        cube = RubikCube()
        self.assertEqual(cube.find_position('G'), 'F')
        self.assertEqual(cube.find_position('W'), 'U')
        self.assertEqual(cube.find_position('R'), 'R')

        self.assertEqual(cube.find_position('G', 'W'), 'FU')
        self.assertEqual(cube.find_position('W', 'G'), 'UF')
        self.assertEqual(cube.find_position('G', 'R'), 'FR')
        self.assertEqual(cube.find_position('R', 'G'), 'RF')

        self.assertEqual(cube.find_position('G', 'W', 'R'), 'FUR')
        self.assertEqual(cube.find_position('G', 'R', 'W'), 'FRU')
        self.assertEqual(cube.find_position('W', 'G', 'R'), 'UFR')
        self.assertEqual(cube.find_position('W', 'R', 'G'), 'URF')
        self.assertEqual(cube.find_position('R', 'G', 'W'), 'RFU')
        self.assertEqual(cube.find_position('R', 'W', 'G'), 'RUF')

        cube = RubikCube()
        cube.move('F')
        self.assertEqual(cube.find_position('R', 'G'), 'DF')

        cube = RubikCube()
        invalid_pieces = {
            (),
            ('W', 'Y'),
            (0, 1),
            ('W', 'G', 'R', 'Y'),
            (('W',),)
        }

        for invalid_piece in invalid_pieces:
            with self.assertRaises(ValueError):
                cube.find_position(invalid_piece)

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
