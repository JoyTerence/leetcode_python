
def min_frogs_croaking(croakOfFrogs):
    hmap = {
        'c': croakOfFrogs.count('c'),
        'r': croakOfFrogs.count('r'),
        'o': croakOfFrogs.count('o'),
        'a': croakOfFrogs.count('a'),
        'k': croakOfFrogs.count('k'),
    }

    if not hmap['c'] == hmap['r'] == hmap['o'] == hmap['a'] == hmap['k']:
        return -1
    
    frogs, ans = 0, 0

    for char in croakOfFrogs:
        hmap[char] -= 1
        if char == 'c':
            frogs += 1
            ans = max(frogs, ans)
        elif char == 'k':
            frogs -= 1
        else:
            if not hmap['c'] <= hmap['r'] <= hmap['o'] <= hmap['a'] <= hmap['k']:
                return -1
    
    return ans

'''
Time: O(N)
Space: O(N)
'''