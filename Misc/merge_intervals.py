'''
In Place Solution
Time: O(NlogN)
Space: O(1)
'''

def merge_intervals(intervals):

    intervals.sort(key = lambda x: x[0])

    i, j = 0, 1

    while j < len(intervals):
        if intervals[i][1] >= intervals[j][0]:
            intervals[i] = [intervals[i], max(intervals[i][1], intervals[j][1])]
            intervals.pop(j)
        else:
            i += 1
            j += 1
    
    return intervals

'''
Not in Place Solution
Time: O(NlogN)
Space: O(N)
'''

def merge_intervals(intervals):

    intervals.sort(key = lambda x: x[0])
    merged = [intervals[0]]

    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged
