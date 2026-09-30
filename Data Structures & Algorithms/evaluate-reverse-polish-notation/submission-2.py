class Solution:
    def solve(self,num1,num2,operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        else:
            return int(num1 / num2)
    def evalRPN(self, tokens: List[str]) -> int:
      stack = []
      op_map = {
        "+", 
        "-", 
        "*",
        "/"
      }  
      for i in tokens:
        if i in op_map:
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(self.solve(num1,num2,i))
        else:
            stack.append(int(i))
      return stack.pop()