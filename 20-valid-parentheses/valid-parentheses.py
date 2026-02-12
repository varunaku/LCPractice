class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d = { "]":"[", ")":"(", "}":"{"}

        for i in range(len(s)):
            if stack and s[i] in d and stack[-1] == d[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0