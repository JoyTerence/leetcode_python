# https://leetcode.com/problems/trapping-rain-water/

def trapping_rain_water(height):
    l, r = 0, len(height)-1
    ans = 0
    left_max, right_max = 0, 0

    while l < r:
        left_max = max(left_max, height[l])
        right_max = max(right_max, height[r])
        
        if left_max < right_max:
            ans += left_max - height[l]
            l += 1
        else:
            ans += right_max - height[r]
            r -= 1
    return ans

'''
Time: O(N)
Space: O(1)
'''
