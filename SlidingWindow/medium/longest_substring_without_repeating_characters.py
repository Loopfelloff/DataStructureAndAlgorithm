class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_length = 0
        alphabet_count = [0] * 1000
        duplicate_count = 0
        first_index, last_index = 0 ,0
        while last_index < len(s):
            already_exists_or_not = alphabet_count[ord(s[last_index])] 
            if already_exists_or_not > 0:
                duplicate_count += 1
            alphabet_count[ord(s[last_index])] += 1
            if duplicate_count == 0:
                current_length = (last_index - first_index) + 1
                max_length = max(max_length , current_length)
            else:
                first_already_exists_or_not = alphabet_count[ord(s[first_index])]
                if first_already_exists_or_not > 1:
                    duplicate_count -= 1
                alphabet_count[ord(s[first_index])] -= 1
                first_index += 1
            last_index += 1
        return max_length

        
def main():
    solution = Solution()
    test_cases = ["abcabcbbabcdef", "bbbbb", "pwwke", 'aaaaaaaaabacdbdddabcdef']
    for case in test_cases:
        print(case)
        print(solution.lengthOfLongestSubstring(case))

main()
