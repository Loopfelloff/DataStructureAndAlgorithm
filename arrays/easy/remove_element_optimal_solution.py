class Solution:
    def removeElement(self, nums: list[int], val: int) -> int :
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] =nums[n-1]
                n -= 1
            else:
                i += 1
        return  i

def main():
    test_cases = [[3,2,2,3] , [0,1,2,2,3,0,4,2]]
    val = [3 , 2]
    for index, test_case in enumerate(test_cases):
        print(Solution().removeElement(test_case , val[index]))

main()

