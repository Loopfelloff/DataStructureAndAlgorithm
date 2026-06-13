class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        def atMax(k):
            i , j = 0 , 0
            res = 0
            n = len(nums)
            for j in range(n):
                nums[j] = k - nums[j]

def main():
    k_val = [2,3 , 0 , 0]
    test_cases = [[1,1,1] , [1,2,3] , [-1,-1,1] , [1]]
    for index, test_case in enumerate(test_cases):
        print(Solution().subarraySum(test_case, k_val[index]))

main()
