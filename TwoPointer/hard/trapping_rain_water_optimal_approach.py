class Solution:
    def trap(self, height : list[int])->int : 
        l , r = 0 , len(height)-1
        maxL , maxR = height[l] , height[r]
        trapped_water = 0
        while l < r : 
            if maxL <= maxR:
                l+=1
                maxL = max(maxL , height[l])
                trapped_water += maxL - height[l]
            else : 
                r -=1
                maxR = max(maxR , height[r])
                trapped_water += maxR - height[r] 
        return trapped_water

if __name__ == "__main__":
    solution = Solution()
    arr = [4,2,0,3,2,5]
    trapped_water = solution.trap(arr)
    print(trapped_water)
