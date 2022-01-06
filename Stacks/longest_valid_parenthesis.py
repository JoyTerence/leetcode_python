def longest_valid_parenthesis(s):

    stack = [-1]
    m = 0

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if stack == []:
                stack.append(i)
            else:
                m = max(m, i-stack[-1])
    
    return m

'''

Time complexity : O(n). n is the length of the given string.

Space complexity : O(n). The size of stack can go up to n.

Explanation:

So begins with -1 (optimistically valid substring could start with 0 index)
Whenever "(" is encountered, assuming valid substring will begin after "(" (but excluding current "("'s position).
Whenever ")" is encountered, top of stack is popped - this takes care of immediately previous "(" 
but optimistic assumption of immediately previous's previous "("'s index came true.
So length is current index - top of stock.
"(" always assume that valid string will be "after" "(",
")" pop top of stack (if not empty) and find length of valid string found. 
If ")" is encountered with empty stack. Assume valid string will begin after ")".
'''