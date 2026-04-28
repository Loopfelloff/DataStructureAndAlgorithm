# this one contains my code for count substrings with k frequency charcaters.
# this code fails actually only passed 527 test cases
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        already_exists = [0] * 1000
        now_contains = [0] * 1000
        i , j , min_e = 0 , 0, 0
        total_duplicate_substrings = 0
        for c in s: 
            already_exists[ord(c)] +=1
        while j < len(s):
            now_contains[ord(s[j])] +=1
            
            if already_exists[ord(s[i])] < k :
                i +=1

            elif now_contains[ord(s[j])] == k:
                ahead_val = len(s) - j
                total_duplicate_substrings += ahead_val
                behind_val = i - min_e 
                total_duplicate_substrings += (ahead_val * (behind_val))
                now_contains[ord(s[i])] -= 1
                already_exists[ord(s[i])] -= 1
                i +=1 
                min_e = i
            j+=1

        return total_duplicate_substrings


def main():
    solution = Solution()
    string_cases = ["abacb" , "abcde" , "ajsrhoebe" , "qkfiuuhd" , "shlvvvx" , "coganww","biikmbqb"]
    string_cases_alt = ["abacb"]
    number_cases = [2 , 1 , 2, 2, 2 , 3, 2]
    number_cases_alt = [2]
    print(list(zip(string_cases , number_cases)))
    for i in range(0, len(string_cases)):
        print(solution.numberOfSubstrings(string_cases[i], number_cases[i]))

main()
