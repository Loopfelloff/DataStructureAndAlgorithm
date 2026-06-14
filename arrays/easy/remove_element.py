class Solution:
    def removeElement(self, nums: list[int], val: int) -> int :
        i , j = 0 , 0
        while j  < len(nums):
            if nums[i] != val : 
                i += 1
            elif nums[i] == val and nums[j] != val : 
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
            j += 1
        return i
    # this approach makes it so that original order of the elements are preserved 
    # the previous approach disrupts that order

def main():
    test_cases = [[3,2,2,3] , [0,1,2,2,3,0,4,2]]
    val = [3 , 2]
    for index, test_case in enumerate(test_cases):
        print(Solution().removeElement(test_case , val[index]))

main()
