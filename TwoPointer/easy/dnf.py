# this one is the dutch national flag problem.
# moving in opposite direction is a variation of two pointer
def dnf(nums):
    low , mid , high = 0 , 0 , len(nums)-1

    while mid <=high:
        if nums[mid] == 0:
            nums[mid] ,nums[low] = nums[low] , nums[mid]
            low +=1
            mid +=1
        elif nums[mid] == 1:
            mid +=1
        elif nums[mid] == 2:
            nums[mid] ,nums[high] = nums[high] , nums[mid]
            high -=1
    print(nums)

if __name__ =="__main__":
    dnf([1,0,1,1,0,0,2,2,0,1,0,2])
