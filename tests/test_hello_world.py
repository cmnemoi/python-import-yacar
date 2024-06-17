import unittest

from src import python_import_yacar

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(python_import_yacar.hello(), "Hello, World! from hello_world.py!")

if __name__ == '__main__':
    unittest.main()