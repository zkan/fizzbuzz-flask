import unittest

from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')


if __name__ == '__main__':
    unittest.main()
