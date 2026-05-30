from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMax(k):
            i , j = 0 , 0 
            n = len(nums)
            hash_val = defaultdict(int)
            res = 0
            for j in range(n):
                hash_val[nums[j]] += 1
                while len(hash_val) > k:
                    hash_val[nums[i]] -= 1
                    if hash_val[nums[i]] == 0:
                        del hash_val[nums[i]]
                    i += 1
                res += j - i + 1
            return res


        return atMax(k) - atMax(k - 1) 

def main():
    test_cases =  [[1,2,1,2,3] , [1,2,1,3,4]]
    second_arg =  [2 ,3]
    for index, case in enumerate(test_cases):
        print(Solution().subarraysWithKDistinct(case , second_arg[index]))

main()
