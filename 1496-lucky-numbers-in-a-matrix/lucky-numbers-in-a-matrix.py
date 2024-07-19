class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minElements = set()
        maxElements = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for matrixRow in matrix:
            minElements.add(min(matrixRow))
        for col in range(cols):
            maxElements.add(max([matrix[row][col] for row in range(rows)]))
        return list(minElements & maxElements)