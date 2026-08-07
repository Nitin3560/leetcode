class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = []
        dire = []
        
        for i in range(n):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        rHead = 0
        dHead = 0

        while rHead < len(radiant) and dHead < len(dire):
            r = radiant[rHead]
            d = dire[dHead]
            rHead += 1
            dHead += 1

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if rHead < len(radiant) else "Dire"