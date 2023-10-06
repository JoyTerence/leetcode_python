
import heapq

def minimum_conference_rooms(intervals):

    intervals.sort(key = lambda x: x[0])

    conferences = [intervals[0][1]]

    for interval in intervals[1:]:
        if conferences[0] > interval[0]:
            heapq.heappush(conferences, interval[1])
        else:
            heapq.heapreplace(conferences, interval[1])
    
    return len(conferences)

'''
Time: O(NLogN)
Space: O(N)
'''