class Solution:
    def searchMatrix(self, matrix, target):
        r, c = len(matrix), len(matrix[0])
        lo, hi = 0, r * c - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            val = matrix[mid // c][mid % c]

            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
