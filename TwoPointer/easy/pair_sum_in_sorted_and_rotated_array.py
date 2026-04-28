# hint : if already sorted array given high probability that it's moving in opposite direction type question
class Solution:
    def pairInSortedRotated(self,arr, target):
        lower , higher = 0 , len(arr)-1 
        if arr[lower] > arr[higher]:
            while arr[lower] >= arr[higher]:
                print(f"lower_val : {lower} , higher_val : {higher} ")
                higher -=1
            lower, higher = higher+1,higher
        print(f"lower : {lower} , higher : {higher} ")
        while lower <= higher + len(arr) and lower < len(arr) and higher >= -(len(arr)):
            if arr[lower] + arr[higher] < target:
                lower +=1
            elif arr[lower] + arr[higher] > target:
                higher -=1
            else:
                return True
        return False
if __name__ == "__main__":

    answer = Solution().pairInSortedRotated([10, 7 ,4 ,1], 9)
    print(answer)


