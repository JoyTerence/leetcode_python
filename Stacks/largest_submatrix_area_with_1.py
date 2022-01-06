
def largest_submatrix_area_with_1(matrix):

    def largest_rect_histogram(heights):
        s = [-1]
        m = 0

        for i in range(len(heights)):
                while s[-1] != -1 and heights[s[-1]] >= heights[i]:
                    m = max(m, heights[s.pop()] * (i-s[-1]-1))
                s.append(i)
            
            while s[-1] != -1:
                    m = max(m, heights[s.pop()] * (len(heights)-s[-1]-1))
            
            return m
    
    ans = 0
    dp = [0] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
        ans = max(ans, largest_rect_histogram(dp))
    
    return ans


'''
Time: O(N * M)
Space: O(M)
'''