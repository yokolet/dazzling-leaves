#
# Question 1
#
LENGTH=256 # List length to store character frequencies

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


#
# Question 3
#
class Graph(object):

    def __init__(self, v):
        """Creates an instance of Graph.
        An argument v is a number of vertices"""
        self.V = v      # number of vertices
        self.edges = [] # a list of all edges

    def addEdge(self, src, dest, weight):
        """Adds edge to this graph"""
        self.edges.append([src, dest, weight])

    def find(self, parent, i):
        """A find method of a Union-Find.
        Returns a parent number"""
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """An union method of a Union-Find.
        Updates parent and rank"""
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def mst(self):
        """Runs Kruskals MST algorithm"""
        self.edges = sorted(self.edges, key=lambda x: x[2])
        result = []
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        i = 0  # index of an edge
        e = 0  # number of vertices processed so far
        while e < self.V - 1:
            src, dest, weight = self.edges[i]
            i += 1
            x = self.find(parent, src)
            y = self.find(parent, dest)
            if x != y:
                result.append([src, dest, weight])
                e += 1
                self.union(parent, rank, x, y)
        return result

BASE = ord('A')
def name_to_index(name):
    """A helper function to convert vertex name to index"""
    return ord(name) - BASE

def index_to_name(index):
    """A helper function to convert index to vertex name"""
    return chr(index + BASE)

def adjacencyList(result):
    """A helper function to create a dictionary from list of lists"""
    adj = {}
    for [src, dest, weight] in result:
        src_name = index_to_name(src)
        dest_name = index_to_name(dest)
        if src_name in adj:
            adj[src_name].append((dest_name, weight))
        else:
            adj[src_name] = [(dest_name, weight)]
    return adj

def question3(G):
    """Given an undirected graph G, finds the minimum spanning tree within G.
    Both input and outputs are adjacency list in a form of dictionary."""
    if not G:
        return None
    v = len(G)
    # given graph is empty
    if v == 0:
        return None

    # constructs a gragh
    g = Graph(v)
    for (src, edges) in G.iteritems():
        for (dest, weight) in edges:
            g.addEdge(name_to_index(src), name_to_index(dest), weight)

    # runs MST
    result = g.mst()

    # creates a dictionary from result
    adj = adjacencyList(result)
    return adj


#
# Question 4
#
class TreeNode(object):
    """Class represents BST node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildBST(T):
    """Builds a binary search tree"""
    size = len(T)
    nodes = [TreeNode(i) for i in range(size)]
    children = [False] * size
    # if row has a value 1 in col, nodes[col] is a child of nodes[row]
    for row in range(size):
        for col in range(size):
            if T[row][col] == 1:
                children[col] = True  # this node has a parent
                if nodes[row].data > nodes[col].data:
                    nodes[row].left = nodes[col]
                else:
                    nodes[row].right = nodes[col]
    return (nodes, children)

def LCA(root, n1, n2):
    """Finds the least common ancestor node"""
    if not root:
        return None
    if root.data > n1 and root.data > n2:
        LCA(root.left, n1, n2)
    elif root.data < n1 and root.data < n2:
        LCA(root.right, n1. n2)
    else:
        return root

def question4(T, r, n1, n2):
    """Given two dimensional data as a binary search tree, values of
    root and two node to be compared, returns the value of the least common
    ancestor value"""
    if not T:
        return None
    if not T[0]:
        return None
    nodes, children = buildBST(T)
    # n1 is not a root but doesn't have any parent
    if r != n1 and not children[n1]:
        return None
    # n2 is not a root but doesn't have any parent
    if r != n2 and not children[n2]:
        return None

    root = nodes[r]
    ancestor = LCA(root, n1, n2)
    return ancestor.data


#
# Question 5
#
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

def search(head, m):
    if not head:
        return [-1, None]
    result = search(head.next, m)
    n = result[0] + 1
    result[0] = n
    if (n == m):
        result[1] = head
    return result

def question5(ll, m):
    """Given a linked list and the mth value,
    find a value of mth Node from the end"""
    result = search(ll, m)
    if not result[1]:
        return -1
    return result[1].data
