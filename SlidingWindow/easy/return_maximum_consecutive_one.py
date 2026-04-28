# i don't think you can go better than this one.
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:

        i , j = 0 , 0
        one_and_zero = [0,0]
        while j < len(nums):
            one_and_zero[nums[j]] += 1
            if one_and_zero[0] >= 1:
                one_and_zero[nums[i]] -= 1
                i+=1
            j +=1
        return (j-i) # usually j - i + 1 is the size of sliding window however, in this particular exameple the reason why we exist the while loop is because j gets overflown from the arrays length making the sliding window's length 1 more than it actaully would've been.

def main():
    solution  = Solution()

    test_cases = [[1,1,0,1,1,1] , [1,0,1,1,0,1]]

    for arr in test_cases:
        print(solution.findMaxConsecutiveOnes(arr))

main()


