# it's not even two pointer solution
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        hash_map = {}
        count = 0
        for i in range(len(nums)-1 , -1 , -1):
            self_count_val = hash_map.get(nums[i] , 0)
            hash_map[nums[i]] = self_count_val + 1
            count += hash_map.get((nums[i]+k) , 0)
            count += hash_map.get((nums[i]-k) , 0)
        return count
