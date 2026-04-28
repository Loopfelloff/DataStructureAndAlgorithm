# i am thinking of doing same direction two pointer solution
# this one is too accepted
class Solution:
    def trap(self, height: list[int]) -> int:
    
        total_sum = 0 
        counting_sum = 0
        i , j = 0 ,1
        while j < len(height):
            if(height[i] <= height[j]):
                i = j
            j += 1
        start_i ,start_j, end_i, end_j = 0 , 1 , len(height)-1 , len(height)-2

        while start_j <= i:
            if(height[start_i] <= height[start_j]):
                total_sum += counting_sum 
                counting_sum = 0
                start_i = start_j
            elif(height[start_i] > height[start_j]):
                counting_sum += height[start_i]-height[start_j]
            start_j += 1
                
        # this shouldnt' interfere but here let's do it for the sake of ease of debugging


        counting_sum = 0
    
        while end_j >= i : 
            if(height[end_j] >= height[end_i]):
                total_sum +=counting_sum 
                counting_sum = 0
                end_i = end_j
            elif(height[end_j] < height[end_i]):
                counting_sum += height[end_i] - height[end_j]
            end_j -= 1


        return total_sum

if __name__ == "__main__":
    solution = Solution()
    arr = [4,2,0,3,2,5] 
    trapped_water = solution.trap(arr)
    print(trapped_water)



               
