# there are quite other solutions that are faster executing than this however with the same time and space complexity. I really don't think there is any point in using other techniques because they are not introducing any new concepts rather it's just normal method using max() function also this folder is dedicated to slidingWindow technique which still has the same time and space complexity so i would rather not use another method.
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        hash_arr = [0]  * 100_000
        i , j = 0 , 0
        count_unique = 0
        while j < len(fruits):
            hash_arr[fruits[j]] += 1
            if hash_arr[fruits[j]] == 1:
                count_unique += 1
            if hash_arr[fruits[i]] == 1 and count_unique > 2:
                hash_arr[fruits[i]] -= 1
                count_unique -= 1
                i += 1
            elif hash_arr[fruits[i]] > 1 and count_unique > 2:
                hash_arr[fruits[i]] -= 1
                i += 1
            j += 1
        return (j - i)



def main():
    solution = Solution()
    test_cases = [[1,2,1] , [0,1,2,2] , [1,2,3,2,2]]
    test_case_one = [[1,2,3,2,2,3,4,3]]
    for case in test_case_one:
        print(solution.totalFruit(case))

main()
