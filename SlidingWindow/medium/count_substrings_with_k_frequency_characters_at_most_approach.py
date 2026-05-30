from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def atMax(k):
            i , j = 0 , 0 
            n = len(s)
            hash_val = defaultdict(int)
            res = 0 
            for j in range(n):
                hash_val[s[j]] += 1 
                while hash_val[s[j]] > k:
                    hash_val[s[i]] -= 1
                    if hash_val[s[i]] == 0:
                        del hash_val[s[i]]
                    i += 1
                res += j - i + 1
            return res

        return atMax(k) - atMax(k-1)

def main():
    test_cases = ["abacb" , "abcde"]
    k_val = [2, 1]
    for index , case in enumerate(test_cases):
        print(Solution().numberOfSubstrings(case , k_val[index]))

main()
