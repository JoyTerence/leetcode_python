
def top_k_frequent(nums, k):
    bucket = [[] for _ in range(len(nums)+1)]
    count = collections.Counter(nums).items()
    for num, freq in count: bucket[freq].append(num)
    flatten = [item for sub in bucket for item in sub]
    return flatten[::-1][:k]

''' 
Time: O(N)
Space: O(N)
'''

def top_k_frequent(nums, k):
    d = collections.defaultdict(int)
    for num in nums:
        d[num] += 1
    arr = []
    for key in d:
        heapq.heappush(arr, (-d[key], key))
    
    op = []
    for i in range(k):
        op.append(heapq.heappop(arr)[1])
    
    return op

'''
Time: O(Nlogk)
Space: O(N+k)
'''