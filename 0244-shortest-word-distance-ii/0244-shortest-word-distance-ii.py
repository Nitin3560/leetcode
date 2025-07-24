class WordDistance(object):

    def __init__(self, wordsDict):
        self.word_indices = {}
        for i, word in enumerate(wordsDict):
            if word not in self.word_indices:
                self.word_indices[word] = []
            self.word_indices[word].append(i)

    def shortest(self, word1, word2):
        indices1 = self.word_indices[word1]
        indices2 = self.word_indices[word2]
        
        i, j = 0, 0
        min_dist = float('inf')
        
        while i < len(indices1) and j < len(indices2):
            index1, index2 = indices1[i], indices2[j]
            min_dist = min(min_dist, abs(index1 - index2))
            
            if index1 < index2:
                i += 1
            else:
                j += 1
        
        return min_dist
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)