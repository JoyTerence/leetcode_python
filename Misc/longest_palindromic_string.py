
def longest_palindromic_string(s):

    def expand_around_center(s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start, end = 0, 0

    for i in range(len(s)):
        odd_pos = expand_around_center(s, i, i)
        even_pos = expand_around_center(s, i, i+1)

        max_len = max(odd_pos, even_pos)

        if max_len > end - start:
            start = i - (max_len - 1)// 2
            end = i + max_len // 2
    
    return s[start:end+1]

'''
Time: O(N^2)
Space: O(1)
'''