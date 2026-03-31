class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            nextRow = [1] * n
            for j in range(n - 2, -1, -1):
                nextRow[j] = nextRow[j + 1] + row[j]
            row = nextRow
        return row[0]
