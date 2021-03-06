import unittest
import solutions

# Anagram check
class TestQuestion1(unittest.TestCase):

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


# the longest palindromic substring
class TestQuestion2(unittest.TestCase):

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


# minimum spanning tree
class TestQuestion3(unittest.TestCase):

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


# the least common ancestor
class TestQuestion4(unittest.TestCase):

    T = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]];

    T2 = [[0, 0, 0, 0, 0, 0, 0],
          [1, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0]];


    def test_none(self):
        self.assertIsNone(solutions.question4(None, 0, 0, 0))

    def test_empty(self):
        self.assertIsNone(solutions.question4([[]], 0, 0, 0))

    def test_example(self):
        r = 3
        n1 = 1
        n2 = 4
        self.assertEquals(solutions.question4(self.T, r, n1, n2), 3)

    def test_orphan(self):
        r = 3
        n1 = 2
        n2 = 4
        self.assertIsNone(solutions.question4(self.T, r, n1, n2))

    def test_root(self):
        r = 3
        n1 = 3
        n2 = 4
        self.assertEquals(solutions.question4(self.T, r, n1, n2), 3)

    def test_bigger_tree_right(self):
        r = 3
        n1 = 4
        n2 = 6
        self.assertEquals(solutions.question4(self.T2, r, n1, n2), 5)

    def test_bigger_tree_left(self):
        r = 3
        n1 = 2
        n2 = 0
        self.assertEquals(solutions.question4(self.T2, r, n1, n2), 1)


# mth node from the end in a linked list
class TestQuestion5(unittest.TestCase):

    def createLinkedList(self, ary):
        node = solutions.Node(ary[0])
        tmp = node
        for i in range(1, len(ary)):
            tmp.next = solutions.Node(ary[i])
            tmp = tmp.next
        return node

    def test_none(self):
        m = 2
        self.assertEquals(solutions.question5(None, 0), -1)

    def test_one(self):
        m = 0
        self.assertEquals(solutions.question5(solutions.Node(0), 0), 0)

    def test_example(self):
        ll = self.createLinkedList([1, 2, 3, 4, 5])
        m = 3
        self.assertEquals(solutions.question5(ll, m), 2)

    def test_example2(self):
        ll = self.createLinkedList([1, 2, 3, 4, 5])
        m = 4
        self.assertEquals(solutions.question5(ll, m), 1)


if __name__ == '__main__':
    unittest.main()
