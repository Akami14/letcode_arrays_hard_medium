""" Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105 """



        
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #отсортируем тогда маленькие и отриц числа будут в начале
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:  # защита от дубликатов 
            #если мы см на 1 и подбираем для нее пары лева и права,
            #а потом сдвинулись +1 и см на др 1 то будут дубликаты из первого случая
                continue

            if nums[i] > 0: # если наш колышек nums[i] больше 0 сума уже будет больше так ост индексы идут правее и числа там больше 0
                break
            n, r = i + 1, len(nums) - 1

            while n < r: # пока не дайдем до конца списка до права
                s = nums[i] + nums[n] + nums[r]
                if s < 0:
                    n += 1 # cсумма - движем левый колышек в право
                elif s > 0:
                    r -= 1 #сумма + движем правый колышек влево назад
                else: #s=0!
                    res.append([nums[i], nums[n], nums[r]])
                    while n < r and nums[n] == nums[n+1]: # чекаем дубликаты (если n =1 и сл n=1 то получим ту же комбинацию что и была)
                        n += 1
                    while n < r and nums[r] == nums[r-1]:
                        r -= 1
                    n += 1
                    r -= 1
        return res



        
