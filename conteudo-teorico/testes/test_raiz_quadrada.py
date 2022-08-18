import unittest

def square(x):
    return x*x

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-2), 4)
        
#rodar o teste: python -m unittest -v