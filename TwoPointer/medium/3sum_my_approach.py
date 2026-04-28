# moving in opposite direction
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        hash_map = {}
        for i in range(0, len(nums)-2):
            j , k = i +1 , len(nums)-1 
            while j<k :
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j +=1
                elif sum >0:
                    k -=1
                elif sum ==0:
                    if((nums[i], nums[j] , nums[k]) not in hash_map):
                        hash_map[(nums[i], nums[j] , nums[k])] = True
                        results.append([nums[i] , nums[j] , nums[k]])
                    j +=1
                    k -=1
        return results 

solution = Solution()
val = solution.threeSum([-100,-70,-60,110,120,130,160])
print(val)
