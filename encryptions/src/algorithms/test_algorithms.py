import unittest
import algorithms as algo


class TestAlgorithms(unittest.TestCase):
    def test_caesar_encode(self):
        self.assertEqual(algo.encode_caesar_cipher("a", 1), "b", "Should be b")
        self.assertEqual(algo.encode_caesar_cipher("a", 2), "c", "Should be b")
        self.assertEqual(algo.encode_caesar_cipher("a", 28), "c", "Should be c")
        self.assertEqual(algo.encode_caesar_cipher("cat dog hello", 28), "ecv fqi jgnnq", "Should be ecv fqi jgnnq")
        self.assertEqual(algo.encode_caesar_cipher("a", 0), "a", "Should be a")
        self.assertEqual(algo.encode_caesar_cipher("a", -1), "Cannot have a negative rotation",
                         "Should be Cannot have a negative rotation")

    def test_caesar_decode(self):
        self.assertEqual(algo.decode_caesar_cipher("a", 1), "z", "Should be z")
        self.assertEqual(algo.decode_caesar_cipher("b", 1), "a", "Should be a")
        self.assertEqual(algo.decode_caesar_cipher("a", 0), "a", "Should be a")
        self.assertEqual(algo.decode_caesar_cipher("a", -1), "Cannot have a negative rotation",
                         "Should be Cannot have a negative rotation")


if __name__ == '__main__':
    unittest.main()
