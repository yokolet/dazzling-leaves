#
# Question 1
#

# List length to store character frequencies
LENGTH=256

def count(s, start, end):
    """Counts frequencies of characters of a given string s
    between start and end(exclusive)"""
    a = [0]*LENGTH
    for i in range(start, end):
        a[ord(s[i])] += 1
    return a

def compare(l0, l1):
    """Compares frequency list l0 and l1 and returns True
    if two lists are identical, otherwise returns False"""
    for i in range(0, LENGTH):
        if l0[i] != l1[i]:
            return False
    return True

def question1(s, t):
    """Given two strings s and t, this function checks whether
    some anagram of t is a substring of s.
    If there're anagram, the function returns True, False otherwise"""
    if not t:
        return False
    M = len(t)
    N = len(s)
    if M == 0:
        return False
    t_counts = count(t, 0, len(t))
    for i in range(0, (N - M) + 1):
        s_counts = count(s, i, i + M)
        if compare(t_counts, s_counts):
            return True
    return False

#
# Question 2
#

def question2(a):
    """Given a string a, returns the longest palindromic substring in a"""
    # edge cases
    if not a:
        return None
    N = len(a)
    if N == 0:
        return None
    if N == 1:
        return a
    
    beginIndex = 0
    maxLen = 1
    table = [[False for j in range(N)] for i in range(N)]

    # base case 1: each single character is a palindrome
    for i in range(N):
        table[i][i] = True

    # base case 2: when characters at index i and i+1 are the same,
    # those are palindromes
    for i in range(N-1):
        if a[i] == a[i+1]:
            table[i][i+1] = True
            beginIndex = i
            maxLen = 2

    # goes over all lengths to the end of the given string
    for l in range(3, N + 1):
        for i in range(N - l + 1):
            j = i + l - 1
            # when substring from i+1 to j-1(i+l-2) is a palindrome,
            # checks i and j(i+l-1) are the same.
            # (a search window gets widen)
            if table[i+1][j-1] and a[i] == a[j]:
                table[i][j] = True
                beginIndex = i
                maxLen = l

    return a[beginIndex:beginIndex+maxLen]
