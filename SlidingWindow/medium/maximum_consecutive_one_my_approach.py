# this is my approach to maximum consecutive ones question
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        i , j = 0,0

        one_and_zero = [0,0]

        while j < len(nums):

            one_and_zero[nums[j]] += 1

            if one_and_zero[0] > k : 

                one_and_zero[nums[i]] -= 1

                i +=1 

            j += 1

        return j - i # the reason why i j-i instead of j - i + 1 for sliding window length is explained in the easy variation of this question

def main():

    solution=Solution()

    test_cases = [[1,1,1,0,0,0,1,1,1,1,0] , [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]]
    test_cases_length = [2 ,3]

    for j in range(len(test_cases)):

        print(solution.longestOnes(test_cases[j], test_cases_length[j]))

main()



