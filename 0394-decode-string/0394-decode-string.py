class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        cur_num = 0
        cur_str = []

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                num_stack.append(cur_num)
                str_stack.append(''.join(cur_str))
                cur_num = 0
                cur_str = []
            elif ch == ']':
                repeat = num_stack.pop()
                prev = str_stack.pop()
                cur_str = [prev + ''.join(cur_str) * repeat]
            else:
                cur_str.append(ch)

        return ''.join(cur_str)

        