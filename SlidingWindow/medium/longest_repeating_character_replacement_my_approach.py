# this is python code my approach
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hash_map = [0] * 26
        i , j = 0 , 0
        max_length = 0
        max_freq = 0 
        while j < n:
            hash_map[ord(s[j]) - ord('A')] += 1
            max_freq  = max(max_freq , hash_map[ord(s[j]) - ord('A')])
            if (j - i + 1) - max_freq > k:
                hash_map[ord(s[i]) - ord('A')] -=1
                i +=1
            max_length = max(max_length , (j-i + 1))
            j+=1
        return max_length
    
def main():
    solution = Solution()
    test_cases = ["ABAB",  "AABABBA" , "ABBB" , "BAAAB"]
    real_case = test_cases[:1]
    required_length = [2, 1 , 2, 2]
    for index,case in enumerate(test_cases):
        print(solution.characterReplacement(case , required_length[index]))

main()
