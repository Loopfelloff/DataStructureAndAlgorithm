class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMax(maxVal : int)->int:
            if maxVal < 0:
                return 0
            i , j = 0 , 0
            res = 0
            value_count = 0
            while j < len(nums):
                value_count += nums[j]
                while value_count > maxVal:
                    if nums[i] == 1:
                        value_count -= 1
                    i += 1

                res += (j-i + 1)
                j += 1

            return res
        return atMax(goal) - atMax(goal-1) 

def main():
    test_cases = [[1,0,1,0,1] , [0,0,0,0,0]]
    goals = [2 , 0]
    for index, item in enumerate(test_cases):
        print(Solution().numSubarraysWithSum(item , goals[index]))


main()
