class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        index1 = index2 = -1
        min_distance = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i
            elif word == word2:
                index2 = i
        
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))
    
        return min_distance