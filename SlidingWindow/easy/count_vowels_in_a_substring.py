from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def atMost(k):
            i , j = 0 , 0
            vow = set("aeiou")
            res = 0
            dict_ = defaultdict(int)
            for j in range(len(word)):
                if word[j] not in vow:
                    i = j + 1
                    dict_ = defaultdict(int)
                    continue
                dict_[word[j]] += 1
                while len(dict_) > k:
                    dict_[word[i]] -= 1
                    if dict_[word[i]] == 0:
                        del dict_[word[i]]
                    i +=1
                res += j - i + 1 
            return res

        return atMost(5) - atMost(4) 

def main():
    test_cases = ["aeiouu" , "unicornarihan" , "cuaieuouac"]
    correct = [2 , 0 , 7]
    print(correct)
    for case in test_cases:
        print(Solution().countVowelSubstrings(case))

main()


