class Solution(object):
    def customSortString(self, order, s):
        count = Counter(s)
        result = []
        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]
        for ch, freq in count.items():
            result.append(ch * freq)

        return ''.join(result)