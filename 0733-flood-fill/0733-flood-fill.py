class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        if source == color:
            return image
        
        def fill(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return
            if image[row][col] != source:
                return
            image[row][col] = color
            fill(row+1, col)
            fill(row-1, col)
            fill(row, col+1)
            fill(row, col-1)
        
        fill(sr, sc)
        return image