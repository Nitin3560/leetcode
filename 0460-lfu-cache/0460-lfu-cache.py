class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}              
        self.groups = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, count = self.cache[key]

        del self.groups[count][key]

        if not self.groups[count]:
            del self.groups[count]

            if self.min_freq == count:
                self.min_freq += 1

        count += 1
        self.cache[key] = [value, count]
        self.groups[count][key] = None

        return value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self.get(key)
            return

        if len(self.cache) == self.cap:
            key_remove, _ = self.groups[self.min_freq].popitem(last=False)
            del self.cache[key_remove]

        self.cache[key] = [value, 1]
        self.groups[1][key] = None
        self.min_freq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)