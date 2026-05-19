class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # stores indices
        max_area = 0

        # add a sentinel bar of height 0 to flush the stack
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                # if stack is empty, width extends from 0 to i-1
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        return max_area

