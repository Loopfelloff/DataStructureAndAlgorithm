# this is the code to remove duplicates from a sorted array
# also uses the fast and slow pointer technique here.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicate_count = False
        count , runner = 0 , 1
        while runner < len(nums) and len(nums) > 1:
            if nums[count] != nums[runner]:
                duplicate_count =False
                count +=1
                nums[count] , nums[runner] = nums[runner] , nums[count]
            elif nums[count] == nums[runner]:
                if duplicate_count is False:
                    count +=1
                    nums[count] , nums[runner] = nums[runner], nums[count]
                    duplicate_count = True
            runner +=1
        return count +1
