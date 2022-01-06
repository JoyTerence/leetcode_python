def largest_rect_in_histogram(heights):

    s = [-1]
    m = 0

    for i in range(len(heights)):
        while s[-1] != -1 and heights[s[-1]] >= heights[i]:
            height = heights[s.pop()]
            width = i - s[-1] - 1
            m = max(m, height * width)
        s.append(i)

    while s[-1] != -1:
        height = heights[s.pop()]
        width = len(heights) - s[-1] - 1
        m = max(m, height * width)
    
    return m

'''
Time: O(N)
Space: O(N)
'''