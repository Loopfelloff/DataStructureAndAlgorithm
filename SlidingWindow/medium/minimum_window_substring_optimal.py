class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        start_i = -1
        i  = 0
        count = 0 
        dict_s = [0] * 256
        dict_t = [0] * 256
        min_range = 100001
        n , m = len(s), len(t)
        for j in range(m):
            dict_t[ord(t[j])] += 1

        for j in range(n):

            dict_s[ord(s[j])] += 1

            if dict_s[ord(s[j])] <= dict_t[ord(s[j])]: # finding unique occurence of such letter
                count += 1
            if count == m: # once this line is true it will be true for all iterations 
                while dict_t[ord(s[i])] == 0 or dict_s[ord(s[i])] > dict_t[ord(s[i])]:
                    if dict_s[ord(s[i])] > dict_t[ord(s[i])]:
                        dict_s[ord(s[i])] -= 1
                    i += 1
                min_val = min(min_range, j-i+1) 
                if min_val != min_range:
                    min_range = min_val
                    start_i = i
        if start_i == -1:
            return ""
        return s[start_i:start_i+min_range]

def main():
    if __name__ == "__main__":
        test_cases = ["ADOBECODEBANC" , "a" , "a" , "aa" , "cabwefgewcwaefgcf"]
        target = ["ABC" , "a" , "aa" , "aa" , "cae"] #last one has cwae as the correct answer
        for index , test_case in enumerate(test_cases):

            print(Solution().minWindow(test_case , target[index]))
main()
