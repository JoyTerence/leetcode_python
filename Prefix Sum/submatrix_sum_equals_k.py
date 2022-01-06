
def submatrix_sum_equals_k(matrix, target):

    r, c = len(matrix), len(matrix[0])

    count = 0

    ps = [[0]*(c+1) for _ in range(r+1)]

    for i in range(1, r+1):
        for j in range(1, c+1):
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i-1][j-1]
    
    for r1 in range(1, r+1):
        for r2 in range(r1, r+1):
            hmap = collections.defaultdict(int)
            hmap[0] = 1
            for col in range(1, c+1):
                s = ps[r2][col] - ps[r1-1][col]
                if s - target in hmap:
                    count += hmap[s-target]
                hmap[s] += 1
    
    return count

'''
Time: O(R^2*C)
Space: O(R*C) 
'''