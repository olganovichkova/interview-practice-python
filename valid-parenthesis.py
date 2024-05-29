def isValid(self, s):
        # s = "(])"
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            if p == ")" or p == "}" or p == "]":
                if len(stack) == 0:
                    return False
                else:
                    last = stack[-1]
                    if last == "(" and p == ")":
                        stack.pop()
                    elif last == "{" and p == "}":
                        stack.pop()
                    elif last == "[" and p == "]":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False

def isValid(s):
    stack = []
    for p in s:
        if p =="(" or p == "{" or p == "[":
            stack.append(p)
        if p == ")" or p == "}" or p == "]":
            if len(stack) == 0:
                return False
            else:
                last = stack[-1]
                if last == "(" and p == ")":
                    stack.pop()
                elif last == "{" and p == "}":
                    stack.pop()
                elif last == "[" and p == "]":
                    stack.pop()
                else:
                    return False
    if len(stack) == 0:
        return True
    return False