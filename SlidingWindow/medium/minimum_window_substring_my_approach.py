from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        i , j = 0 , 0 
        ever_changed = False
        true_i , true_j = 0 , 0 
        min_size = 100001
        dict_s = [0] * 256
        dict_t = [0] * 256 
        count = 0
        for j in range(len(t)):
            dict_t[j] += 1
        for j in range(len(s)):
            dict_s[j] += 1
            if dict_s[j] <= dict_t[j]:
                count += 1
            if count == len(set(t)):
                ever_changed = True
                true_minimimum  = min(min_size , j-i+1)
                if true_minimimum != min_size:
                    min_size = true_minimimum
                    true_i , true_j = i , j 
                i = j + 1
                count = 0 
        if ever_changed is True:
            return s[true_i : true_j + 1]
        else:
            return ""

def main():
    if __name__ == "__main__":
        test_cases = ["ADOBECODEBANC" , "a" , "a" , "aa"]
        target = ["ABC" , "a" , "aa" , "aa"]
        for index , test_case in enumerate(test_cases):
            print(Solution().minWindow(test_case , target[index]))

main()
