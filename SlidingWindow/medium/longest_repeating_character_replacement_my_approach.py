# this is python code my approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = [0] * 10_000         
        unique_char = 0
        i , j = 0 , 0
        while j < len(s): 
            hash_map[ord(s[j])] += 1 
            if hash_map[ord(s[j])] == 1:
                unique_char +=1 
            if unique_char > k:
                hash_map[ord(s[i])] -= 1
                unique_char -=1 # This logic ain't correct as well 
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
