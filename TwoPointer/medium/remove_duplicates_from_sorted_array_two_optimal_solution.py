# this optimal solution doesn't use two pointer solution
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for n in nums : 
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i+=1
        return i

if __name__ == "__main__":
    solution = Solution()
    check_array = [1,1,1,2,2,2,3,3]
    correct_array = [1,1,2,2,3,3]
    return_index = solution.removeDuplicates(check_array)
    for i in range(0,return_index):
        assert check_array[i] == correct_array[i]
    print("the solution was correct " , check_array[:return_index])

