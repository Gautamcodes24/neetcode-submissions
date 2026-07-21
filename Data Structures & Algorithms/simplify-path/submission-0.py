class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        print(paths)
        for p in paths:
            if p == "..":
                if stack:
                    stack.pop()
            elif p != "" and p != ".":
                stack.append(p)
        return "/" + "/".join(stack)