# should preserve the relative order of non-zero array elements.
def move_zeros_to_end(nums):
    low , run = 0, 0
    while run <= len(nums)-1:
        if nums[run] !=0:
            nums[run] , nums[low] = nums[low], nums[run]
            low +=1
        run +=1
    print(nums)

if __name__ == '__main__':
    move_zeros_to_end([12,0,0,13,0,14,15])
