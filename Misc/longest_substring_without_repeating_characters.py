
def longest_substring_without_repeating_characters(s):

    i, ans = 0, 0

    hmap = {}

    for j in range(len(s)):
        if s[j] in hmap:
            i = max(i, hmap[s[j]]+1)
        ans = max(ans, j - i + 1)

        hmap[s[j]] = j
    
    return ans

'''
Time: O(N)
Space: O(N)
'''