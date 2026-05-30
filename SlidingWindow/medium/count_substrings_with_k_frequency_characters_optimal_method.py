# this one contains my code for count substrings with k frequency charcaters.
from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        res = (n + 1) * n // 2 # if / is only used you get 4.0 instead of 4 so just precaution i suppose 
        count = defaultdict(int)
        i = 0
        for j in range(n):
            count[s[j]] +=1
            while count[s[j]] >= k:
                count[s[i]] -= 1
                i += 1
            res -= j - i + 1
        return res


def main():
    solution = Solution()
    string_cases = ["abcda","abacbe" , "abcde" , "ajsrhoebe" , "qkfiuuhd" , "shlvvvx" , "coganww","biikmbqb"]
    number_cases = [2,2 , 1 , 2, 2, 2 , 3, 2]
    print(list(zip(string_cases , number_cases)))
    for i in range(0, len(string_cases)):
        print(solution.numberOfSubstrings(string_cases[i], number_cases[i]))

main()

