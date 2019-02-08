class Solution:
    def isValid(self, s: 'str') -> 'bool':
        openList = ["[", "{", "("]
        closeList = ["]", "}", ")"]
        stack = []
        pos = 0
        if not s:
            return True
        for i in s:
            # print("printing the chars:",i)
            if i in openList:
                stack.append(i)
                # print("stack:", stack)
            elif i in closeList:
                pos = closeList.index(i)
                # print("printing pos of bracket in closelist:",pos)
                # print("length of the stack:",len(stack))
                if ((len(stack) > 0) and (openList[pos] == stack[len(stack) - 1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


obj = Solution()
print('Valid Parantheses:', obj.isValid('{}]'))
