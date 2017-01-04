# Explanations of questions

## Question1: Substring Anagram

Given two strings, s and t, `anagram_check.py` tests whether some anagram of t
is a substring of s. If t is the anagram substring, a function question1
returns True, otherwise, it returns False.

### Considerations

- Input and Output

    * Input: two strings
    * Output: True or False

- Assumption

    * Two strings s and t are all ASCII characters (maximum 256)
    * s is longer than t

- Edge cases

    A string t is None or empty

- Solution

    1. Finds a character frequency in t and saves in a list
    2. Finds a character frequency a search window in s and saves in a list
    3. If both frequency list are identical, t's anagram is a substring of s
    4. Returns True if t's anagram is a substring of s.
    5. If not, shfts the search window by 1
    6. Repeats 2-4 by the end

- A reason behind the solution

    Under an assumption that all input characters are ASCII, those can fit in
    a list of length 256. No matter how long the string is, the frequency list
    will have the fixed size. Comparisons of the pattern t and the same window
    size substring in s will be done in constant time. This is the reason fixed
    size lists were used here.

- Complexities

    * Runtime: O(n)
    * Space: O(1), (It is big-theta of 256, which is considered O(1))



## Question2: Longest Palindromic Substring

Given a string a, find the longest palindromic substring contained in a.

### Considerations

- Input and Output

    * Input: a string
    * Output: the longest palindromic substring (may be a whole string)

- Edge cases

    A given string is None or empty

- Solution

    Keeps tracking boolean table[i][j] whose value is True if a substring from
    index i to j is a palindrome, otherwise False.

    1. initializes the table[n][n] (n is a length of given string s)
    2. (base case 1) sets True to table[i][i] since a single letter is a palindrome
        of length one
    3. (base case 2) checks the length two substrings and sets True if two letters
        are the same
    4. starting from length 3 substrings, checks whether it is palindrome or not based on
        previous substring length results.
    5. goes over all lengths up to n

- A reason behind the solution

    If comparison is done without the table, the solution will be O(n^3).
    Introduing the table will cut down the performance to O(n^2) while space
    complexity will increase from 1 to O(n^2). If the string length gets longer,
    the difference between O(n^3) and O(n^2) grows big. That's why this solution
    uses the table to save previous results.

- Complexities

    * Runtime: O(n^2)
    * Space: O(n^2)


## Question3: Minimum Spanning Tree in Undirected Graph

Given an undirected graph G, find the minimum spanning tree within G

### Considerations

- Input and Output

    * Input: an adjacency list
    * Output: an adjacency list

    an adjacency list sample:

    ```python
    {'A': [('B', 2)],
     'B': [('A', 2), ('C', 5)],
     'C': [('B', 5)]}
    ```

- Edge cases

    * A given graph is None or empty
    * 