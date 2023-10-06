from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # number of characters that a group of words occupy is
        # numTotalLetters + words - 1 (for spaces)
        # The moment a new word causes this computation to exceed max width is when we introduce a new row
        # Spread the spaces of the remainder of maxwidth and this computation as spaces for each word in a round robin left to right 
        
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        
        remainder = ' '.join(cur)
        remainder += ' ' * (maxWidth - len(remainder))
        
        return res + [remainder]

'''
Time: O(N)
Space: O(N)
'''