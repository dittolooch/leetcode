"""
https://leetcode.com/problems/container-with-most-water/
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water_volume = 0 
        front_index = 0
        back_index = len(height) - 1 
        while True:
            container_width = back_index - front_index
            if height[front_index] > height[back_index]:
                water_volume = height[back_index] * container_width
                back_index -= 1
            else:
                water_volume = height[front_index] * container_width
                front_index += 1
            if water_volume > max_water_volume:
                max_water_volume = water_volume 

            if front_index >= back_index:
                return max_water_volume

# Errors
# 1. naming variables to one that's used by the question
# 2. back_index should be len(arr) - 1
# 3. move the front/back pointer, whichever is shorter
