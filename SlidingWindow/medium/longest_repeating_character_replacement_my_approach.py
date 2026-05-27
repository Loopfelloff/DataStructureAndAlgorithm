# this is python code my approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = [0] * 10_000         
        unique_char = 0
        max_alphabet = 0 
        i , j = 0 , 0
        while j < len(s): 
            print(i,  j)
            hash_map[ord(s[j])] += 1 
            max_alphabet = max(max_alphabet , hash_map[ord(s[j])])
            if hash_map[ord(s[j])] == 1:
                unique_char +=1 
            if unique_char > k:
                hash_map[ord(s[i])] -= 1
                unique_char -=1
                i += 1
            j += 1
        return (j-i)
    
def main():
    solution = Solution()
    test_cases = ["ABAB",  "AABABBA"]
    real_case = test_cases[:1]
    required_length = [2, 1]
    for index,case in enumerate(test_cases):
        print(solution.characterReplacement(case , required_length[index]))

main()
