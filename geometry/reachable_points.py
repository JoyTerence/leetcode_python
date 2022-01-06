
def reachable_points(sx, sy, tx, ty):
    while tx >= sx and ty >= sy:
        if tx == ty:
            return tx == sx
        elif tx > ty:
            if ty > sy:
                tx %= ty
            else:
                return (tx-sx)%ty == 0
        else:
            if tx > sx:
                ty %= tx
            else:
                return (ty-sy)%tx == 0

    return False

'''
Time: O(log(max(tx, ty)))
Space: O(1)
'''