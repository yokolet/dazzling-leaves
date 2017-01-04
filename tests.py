import unittest
import solutions

class TestAnagramCheck(unittest.TestCase):

    def test_none(self):
        self.assertFalse(solutions.question1('any', None))

    def test_empty(self):
        self.assertFalse(solutions.question1('any', ''))

    def test_example(self):
        s = 'udacity'
        t = 'ad'
        self.assertTrue(solutions.question1(s, t))

    def test_on_last_index(self):
        s = 'udacity'
        t = 'ity'
        self.assertTrue(solutions.question1(s, t))
        
    def test_example_to_fail(self):
        s = 'udacity'
        t = 'ai'
        self.assertFalse(solutions.question1(s, t))


class TestLongestPalindromicSubstring(unittest.TestCase):

    def test_none(self):
        a = None
        self.assertIsNone(solutions.question2(a))

    def test_empty(self):
        a = ''
        self.assertIsNone(solutions.question2(a))

    def test_single_char(self):
        a = 'a'
        self.assertEqual(solutions.question2(a), a)

    def test_string_is_a_palindrome(self):
        a = 'testtset'
        self.assertEqual(solutions.question2(a), a)

    def test_substring_is_a_palindrome(self):
        a = 'atesttsets'
        self.assertEqual(solutions.question2(a), 'testtset')

    def test_two_palindromes(self):
        a = 'atesttsetsss'
        self.assertEqual(solutions.question2(a), 'testtset')

    def test_same_size_palindromes(self):
        a = 'aaalllsss'
        self.assertEqual(solutions.question2(a), 'sss')


if __name__ == '__main__':
    unittest.main()
