class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        operations = {
            '+': lambda x, y: x + y,
            '*': lambda x, y: x * y,
            '-': lambda x, y: x - y,
        }

        def compute(left, right):
            result = []
            for i in range(left, right+1):
                op = expression[i]
                if op not in operations:
                    continue
            
                result = result + [operations[op](num1, num2) for num1 in compute(left, i-1) for num2 in compute(i+1, right)]
            return result or [int(expression[left:right+1])]

        return compute(0, len(expression)-1)

s = Solution()

print(s.diffWaysToCompute("2*3-4*5"))
