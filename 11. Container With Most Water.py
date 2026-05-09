"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104 """


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 # задаем нач  индексы лева и права
        max_area = 0
        while l < r: #пока лево и право не встретились
            current_area = min(height[l], height[r]) * (r - l)
            max_area = max(max_area, current_area) 
            # Проверчяем сл пары и двигаемся к центру
            if height[l] < height[r]: # двигаем левый индекс если левая высота меньше правойй что б максимизировать высоту
                l += 1
            else:
                r -= 1

        return max_area




"""
other solutions
from itertools import combinations
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #candidates = combinations([el for el in range(len(height))] , 2)
        S_max = 0
        for pivot in combinations([el for el in range(len(height))] , 2):
            w = pivot[1]-pivot[0]
            if height[pivot[0]] >= height[pivot[1]]:
                m_h = height[pivot[1]]
            else:
                m_h = height[pivot[0]]
            S = w*m_h
            S_max = max(S_max, S)
           # if S > S_max:
            #    S_max=S
        return S_max
 class Solution:
    def maxArea(self, height: List[int]) -> int:
        distance = len(height)
        S_max = 0
        for i in range(distance):
            for j in range(i + 1, distance):
                S = min(height[i], height[j]) * (j - i)
                S_max = max(S_max, S)
        return S_max
"""
