
def russian_envelopes(envelopes):

    envelopes.sort(key = lambda x: (x[0], -x[1]))

    sub = []
    for envelope in envelopes:
        idx = bisect_left(sub, envelope[1])
        if idx == len(sub):
            sub.append(envelope[1])
        else:
            sub[idx] = envelope[1]
    
    return len(sub)

'''
Time: O(NLogN)
Space: O(N)
'''