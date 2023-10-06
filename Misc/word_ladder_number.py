

import collections

def word_ladder_number(beginword, endword, wordList):

    n = len(beginword)

    d = collections.defaultdict(list)

    for word in wordList:
        for i in range(n):
            d[word[:i] + "*" + word[i+1:]].append(word)
    
    q = collections.deque()
    q.append([beginword, 0])
    visited = set()

    while q:
        ele, level = q.popleft()

        if ele == endword:
            return level + 1
        else:
            for i in range(n):
                for candidate in d[ele[:i]+"*"+ele[i+1:]]:
                    if candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, level+1))
            d[ele[:i]+"*"+ele[i+1:]] = [] # not really needed
    return 0

'''
Time Complexity: O(M^2 * N),

where M is the length of each word and N is the total number of words in the input word list.

For each word in the word list, we iterate over its length to find all the intermediate words corresponding to it. 
Since the length of each word is M and we have N words, the total number of iterations the algorithm takes to create d is M*N. 
Additionally, forming each of the intermediate word takes O(M) time because of the substring operation used to create the new string. 
This adds up to a complexity of O(M^2*N).

Breadth first search in the worst case might go to each of the N words. 
For each word, we need to examine M possible intermediate words/combinations. 
Notice, we have used the substring operation to find each of the combination. 
Thus, M combinations take O(M^2) time. As a result, the time complexity of BFS traversal would also be O(M^2*N)

Combining the above steps, the overall time complexity of this approach is O(M^2 * N)

Space Complexity: O(M^2 * N)
'''