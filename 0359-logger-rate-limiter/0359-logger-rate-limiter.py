class Logger:

    def __init__(self):
        self.q = deque()
        self.next_allowed = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q and self.q[0][1] <= timestamp:
            old_msg, old_expire = self.q.popleft()
            if self.next_allowed.get(old_msg) == old_expire:
                del self.next_allowed[old_msg]

        if message in self.next_allowed and self.next_allowed[message] > timestamp:
            return False  

        expire_time = timestamp + 10
        self.next_allowed[message] = expire_time
        self.q.append((message, expire_time))
        return True

