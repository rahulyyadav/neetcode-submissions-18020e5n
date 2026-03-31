class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = [] 

        def backTrack(openN, ClosedN):

            if openN == ClosedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backTrack(openN + 1, ClosedN)
                stack.pop()
            if ClosedN < openN:
                stack.append(')')
                backTrack(openN, ClosedN + 1)
                stack.pop()
        
        backTrack(0, 0)
        return res

        
            