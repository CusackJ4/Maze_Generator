import unittest
from maze_class import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_create_cells2(self):
        num_cols = 50
        num_rows = 13
        m2 = Maze(5, 3, num_rows, num_cols, 30, 40)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )

    def test_wall_removal(self):
        n_rows = 12
        n_cols = 16
        m = Maze(50, 50, n_rows, n_cols, 50, 50)
        entrance = m._Maze__cells[0][0]
        self.assertFalse(entrance.has_top_wall, "Entrance should have no top wall")

        exit_cell = m._Maze__cells[n_cols - 1][n_rows - 1]
        self.assertFalse(exit_cell.has_bottom_wall, "Entrance should have no top wall")
    
    def test_cell_unvisited(self):
        n_rows = 12
        n_cols = 16
        m = Maze(50, 50, n_rows, n_cols, 50, 50)
        first_block = m._Maze__cells[0][0]
        self.assertFalse(first_block.visited, "first_block should be visited")

        

if __name__ == "__main__":
    unittest.main()