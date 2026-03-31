class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        relation = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in relation: 
                if stack and stack[-1] == relation[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False