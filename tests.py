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

class TestMinimumSpanningTree(unittest.TestCase):

    def test_none(self):
        G = None
        self.assertIsNone(solutions.question3(G))

    def test_empty(self):
        G = {}
        self.assertIsNone(solutions.question3(G))

    def test_example(self):
        G = {'A': [('B', 2)],
             'B': [('A', 2), ('C', 5)],
             'C': [('B', 5)]}
        expected = {'A': [('B', 2)],
                    'C': [('B', 5)]}
        self.assertEquals(solutions.question3(G), expected)

    def test_more_edges(self):
        G = {'A': [('B', 1), ('C', 5), ('D', 4)],
             'B': [('A', 1), ('C', 3), ('D', 2)],
             'C': [('A', 5), ('B', 3), ('D', 1)],
             'D': [('A', 4), ('B', 2), ('C', 1)]}
        expected = {'A': [('B', 1)],
                    'C': [('D', 1)],
                    'B': [('D', 2)]}
        self.assertEquals(solutions.question3(G), expected)


if __name__ == '__main__':
    unittest.main()
