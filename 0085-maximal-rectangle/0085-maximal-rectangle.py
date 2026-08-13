class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:

            for col in range(cols):
                if row[col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            max_area = max(max_area, self.Area(heights))

        return max_area


    def Area(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            currheight = 0 if i == len(heights) else heights[i]

            while stack and currheight < heights[stack[-1]]:
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area