class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_tank = 0
        current_tank = 0
        start_index = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            current_tank += gain
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        return start_index if total_tank >= 0 else -1

        