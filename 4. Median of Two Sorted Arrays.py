""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106 """

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        
        # Функция для поиска k-го элемента (по счету, начиная с 1)
        def get_kth_element(k):
            idx1, idx2 = 0, 0 # Текущие границы в массивах
            
            while True:
                # пока в массивах есть ел
                if idx1 == len(nums1):
                    return nums2[idx2 + k - 1]
                if idx2 == len(nums2):
                    return nums1[idx1 + k - 1]
                
                # 2. Базовый случай: ищем самый первый элемент
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])
                
                # 3. Шаг: сравниваем элементы на позиции k // 2
                step = k // 2
                # Берем элемент или "бесконечность", если массив короче шага
                new_idx1 = min(idx1 + step, len(nums1)) - 1
                new_idx2 = min(idx2 + step, len(nums2)) - 1
                
                val1 = nums1[new_idx1]
                val2 = nums2[new_idx2]
                
                # Отбрасываем ненужную часть того массива, где значение меньше
                if val1 <= val2:
                    # Количество реально отброшенных элементов
                    k -= (new_idx1 - idx1 + 1)
                    idx1 = new_idx1 + 1
                else:
                    k -= (new_idx2 - idx2 + 1)
                    idx2 = new_idx2 + 1
        # если масив из нечетного кол-ва элементов лево и право совпадут, если чет то как сред ареф расчитается
        left_mid = get_kth_element((total_len + 1) // 2) # (5+1)//2=3
        right_mid = get_kth_element((total_len + 2) // 2)  #(5+2)//2=3
        
        return (left_mid + right_mid) / 2.0
