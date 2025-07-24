from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        new_nums = [[val] for val in nums]

        while len(new_nums) > 1:
            result = []
            firstptr = 0
            secondptr = 1
            nums_len = len(new_nums) - 1
            while secondptr <= nums_len:
                merge_result = self.merge(new_nums[firstptr], new_nums[secondptr])
                result.append(merge_result)
                firstptr += 2
                secondptr += 2
            if secondptr == len(new_nums):
                result.append(new_nums[-1])
            new_nums = []
            for res in result:
                new_nums.append(res)
        [num] = new_nums
        return num

    def merge(self, left_list, right_list):
        left_cursor = right_cursor = 0
        ret = []

        while left_cursor < len(left_list) and right_cursor < len(right_list):
            if left_list[left_cursor] < right_list[right_cursor]:
                ret.append(left_list[left_cursor])
                left_cursor += 1
            else:
                ret.append(right_list[right_cursor])
                right_cursor += 1

        # append what is remained in either of the lists

        ret.extend(left_list[left_cursor:])
        ret.extend(right_list[right_cursor:])

        return ret

result = Solution().sortArray([5,2,3,1,50,86,84,80,37,5,66,6,3,4,9,0,4,8,8,1,2,3,5,2,34,56,532,45])
print(result)