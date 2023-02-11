'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) 
and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
'''

def count_sorted_vowel_strings(n):

    # 5 vowels
    dp = [[0] * 6 for _ in range(n+1)]

    for vowel in range(1, 6):
        dp[1][vowel] = vowel
    
    for n_value in range(1, n+1):
        dp[n_value][1] = 1
    
    for i in range(2, n+1):
        for j in range(2, 6):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
    return dp[n][5]

'''
Time: O(N)
Space: O(N)
'''