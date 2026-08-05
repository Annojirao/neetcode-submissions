class Solution:
    def isValid(self, s: str) -> bool:
        mapping_dict = {
            '{' : '}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for char in s:
            if char in mapping_dict.keys():
                stack.append(char)
            elif char in mapping_dict.values():
                if len(stack)> 0:
                    pop_key = stack.pop()
                else:
                    return False
                if mapping_dict.get(pop_key) != char:
                    return False
        return len(stack) == 0 and True