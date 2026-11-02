import unittest

import numpy as np

from task import Task


class TestTask(unittest.TestCase):
    def test_resolution(self):
        task = Task(size=10)

        # Résoudre le système Ax = B
        task.work()

        # Vérifier que Ax est égal à B
        np.testing.assert_allclose(
            task.a @ task.x,
            task.b,
            rtol=1e-7,
            atol=1e-10,
        )


if __name__ == "__main__":
    unittest.main()
