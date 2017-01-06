# Explanations of questions

## Question 1: Substring Anagram

Given two strings, s and t, `anagram_check.py` tests whether some anagram of t
is a substring of s. If t is the anagram substring, a function question1
returns True, otherwise, it returns False.

### Considerations

- Input and Output

    * Input: two strings
    * Output: True or False

- Assumptions

    * Two strings s and t are all ASCII characters (maximum 256)
    * s is much longer than t

- Edge cases

    A string t is None or empty

- Solution

    1. Finds a character frequency in t and saves in a list
    2. Finds a character frequency a search window in s and saves in a list
    3. If both frequency list are identical, t's anagram is a substring of s
    4. Returns True if t's anagram is a substring of s.
    5. If not, shifts the search window by 1
    6. Repeats 2-4 by the end

- Reasons behind the solution

    Under an assumption that all input characters are ASCII, those can fit in
    a list of length 256. No matter how long the string is, the frequency list
    will have the fixed size. Comparisons of the pattern t and the same window
    size substring in s will be done in constant time. This is the reason fixed
    size lists were used here.

- Complexities

    M: length of t, N: length of s

    * Runtime: O(MN) -- from the assumption, M is much smaller than N, O(MN)
    * Space: O(1) --  big-theta of 256, which reduces to O(1)



## Question 2: Longest Palindromic Substring

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
    4. starting from length 3 substrings, checks whether it is palindrome or not
        based on previous substring length results.
    5. goes over all lengths up to n

- Reasons behind the solution

    If comparison is done without the table, the solution will be O(N^3).
    Introducing the table will cut down the performance to O(N^2) while space
    complexity will increase from 1 to O(N^2). If the string length gets longer,
    the difference between O(N^3) and O(N^2) grows big. That's why this solution
    uses the table to save previous results.

- Complexities

    * Runtime: O(N^2)
    * Space: O(N^2)


## Question 3: Minimum Spanning Tree in Undirected Graph

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

- Assumptions

    * All vertices are connected (no island).
    * Vertex names are uppercase alphabets.

- Edge cases

    * A given graph is None or empty

- Solution

    This solution uses Kruskal's Minimum Spanning Tree Algorithm

    1. Constructs a Graph object from a given adjacency list
    2. Sorts all edges in non-descreasing order by a weight
    3. Chooses the smallest edge
    4. Checks if adding the edge creates a cycle or not by Union-Find
    5. If the cycle won't be created, adds the edge to a result
    6. Chooses the smallest edge except previously chosen
    7. repeats 4 to 6

- Reasons behind the solution

    For minimum spanning tree solution, there are two major algorithms,
    Prim and Kruskal. Both works well, but we should consider what the given
    graph's shape is. If the graph is sparse, Kruskal's algorithm is better for
    its simple implementation. If the graph has a lot of edges, Prim's algorithm
    runs faster since it doesn't need to sort all edges.

    Since this problem doesn't mention about how many edges are in the graph,
    Kruskal's algorithm was used because of its simplicity.

    Another minor consideration is mapping vertex name to index. Keeping edges in
    a list makes code much more simpler. For this reason, internal experssion uses
    indices instead of vertex names.

- Complexities

    E: number of edges, V: number of vertices

    * Runtime: O(E log(E)) -- for sorting O(E log(E)), for looping O(E)
    * Space: O(V + E) -- for Union-Find it uses 2*V, for graph E, for result E


## Question 4: The least common ancestor in binary search tree (BST)

Given two nodes in BST, find the least common ancestor in the BST

### Considerations

- Input and Output

    * Input: 2D matrix (BST), root value, and two node values
    * Output: an integer respresents a value of the lesat common ancestor

- Assumptions

    * All values in the BST are integers.
    * The tree has BST properties

- Edge cases

    * Given BST is None or empty
    * Given node value is not in BST

- Solution

    1. Starts from root node, compare root data and given two values
    2. If both values are less than root value, moves to left
    3. If both values are greater then root value, moves to right
    4. If none of above, returns root

- Reasons behind the solution

    Without constructing BST, the solution looks up matrix. Each row number
    in matrix corresponds to node data. If the root is 3, the 4th row will be
    the starting point (zero based). Looking at this row, the solution finds
    left or right child row. Next step looks at the child row and finds
    child's left or right child row.

    Given tree has properties of BST, so three cases should be considered.
    Both are greater than root, both are less than root, root is between two.
    Comparing values (row number), it's clear to go left or right next.
    The given example has an orphan node, 2. When 2 is one of given two values,
    there's no common ancestor. To know the node is orphan or not, the solution
    tests whether the node is a part of BST or not before tree is searched.

- Complexities

    * Runtime: O(N) -- O(2N) for child tests, O(N) to find left or right child,
        and O(log(N)) to search BST. In total, O(3N + log(N)), which reduces to O(N).
    * Space: O(N) -- there's no additional data structure explicitly. However,
        LCA function uses O(N) additional space for recursive calls.
        (# of stack frames) * (space per statck frame) = N * 1 = N


## Question 5: The mth element from the end in a linked list

Given a linked list and the number expresses mth, find the mth element from the end.

### Considerations

- Input and Output

    * Input: a linked list and integer (mth)
    * Output: a value(integer) of the mth element from the end

- Assumptions

    * the integer for mth is zero or positive
    * the integer for mth is less than the length of the linked list
    * if no node is found, return value is -1

- Edge case

    * Given linked list is None

- Solution

    The solution uses a recursive call.

    1. Iterates to the end to find the length of the linked list
    2. When it reaches to the end, returns [-1, None].
        the first element is a reverse order, the second element is a Node
    3. While coming back to the head, counts up a reverse order and compares m and n.
        if m and n are the same, saves current node to the second argument.
    4. When it reaches back to the head, the second element of the return value
        is the answer.

- Reasons behind the solution

    This solution performes only one iteration with theta-of 2 space complexity.
    There's another solution to iterate the linked list over twice; to know the length,
    then find the node. Compared to this, the solution is better when the linked list
    is really long.

- Complexities

    * Runtime: O(N)
    * Space: O(N) -- For return data, O(2) is used in search function.
        Additionally, it uses recursive calls, so it need O(N) space, which is
        calculated by (# of stack frames) * (space per statck frame) = N * 1 = N
