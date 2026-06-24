class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        val= 0
       
        for s in tokens:
            if not s in '+*-/':
                stack.append(int(s))

            else:
                b = stack.pop()
                a = stack.pop()
                

                if s == '+':
                    val = a + b
                    stack.append(val)
                elif s == '*':
                    val = a * b
                    stack.append(val)
                elif s == '-':
                    val = a - b
                    stack.append(val)
                elif s == '/':
                    val = a / b
                    stack.append(int(val))
        return stack[0]
                