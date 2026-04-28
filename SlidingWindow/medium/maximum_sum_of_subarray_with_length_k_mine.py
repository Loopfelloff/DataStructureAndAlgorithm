# let's solve this frist question
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        first_item_index, last_item_index= 0 , k-1
        duplicate_item_number = 0
        current_sum = 0
        max_sum = 0 
        hash_map ={} 
        for i in range(first_item_index , last_item_index + 1):
            current_sum += nums[i]
            item_exists_in_hash_map = hash_map.get(nums[i] , 0) 
            if item_exists_in_hash_map > 0:
                duplicate_item_number +=1
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        while last_item_index < len(nums)-1:
            if duplicate_item_number == 0:
                max_sum = max(max_sum , current_sum)
            current_sum = current_sum - nums[first_item_index] + nums[last_item_index+1]
            incremented_item_exists_or_not = hash_map.get(nums[last_item_index+1],0)
            if incremented_item_exists_or_not > 0:
                duplicate_item_number += 1
            hash_map[nums[last_item_index+1]] = hash_map.get(nums[last_item_index+1],0) + 1
            decremented_item_exists_or_not = hash_map.get(nums[first_item_index] , 0)
            if decremented_item_exists_or_not > 1:
                duplicate_item_number -= 1
            hash_map[nums[first_item_index]] -= 1
            last_item_index +=1 
            first_item_index +=1
        return max(max_sum , current_sum) if duplicate_item_number ==0 else max_sum


def main():
    test_cases = [
[1,1,1,7,8,9] ,
[1,5,4,2,9,9,9],
[4,4,4, 1],
[1,1,2,2]
            ]
    solution  = Solution()
    for arr in test_cases:
        print(arr)
        returned_val = solution.maximumSubarraySum(arr , 3)
        print(returned_val)

main()
