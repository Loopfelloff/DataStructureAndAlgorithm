from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        i, j = 0, 0
        n = len(word)
        vow = set("aeiou")
        res = (n+1) * n // 2 
        dict_ = defaultdict(int)
        non_dict_ = defaultdict(int)
        for j in range(n):
            if word[j] not in vow:
                non_dict_[word[j]] += 1
            else:
                dict_[word[j]] += 1
            while len(dict_) == 5:
                dict_[word[i]] -= 1
                if dict_[word[i]] == 0:
                    del dict_[word[i]]
                i += 1
            res -= j - i + 1
        return res
            

def main():
    test_cases = ["aeiouu" , "unicornarihan" , "cuaieuouac"]
    correct = [2 , 0 , 7]
    print(correct)
    for case in test_cases:
        print(Solution().countVowelSubstrings(case))

main()



