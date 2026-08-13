class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])

        words.discard(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue

                    new = word[:i] + c + word[i + 1:]

                    if new in words:
                        q.append((new, steps + 1))
                    

                        words.remove(new)

        return 0