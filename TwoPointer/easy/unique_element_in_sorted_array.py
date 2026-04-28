# for finding the unique element in the sorted array.
# moving in the same direction
# modify the array in place,
# same direction with fast/slow pointer approach
def move_unique_to_left(nums):
    point , runner = 0 , 0
    while runner < len(nums):
        if(nums[point] == nums[runner]):
            runner +=1
        else:
            point +=1
            nums[point],nums[runner]= nums[runner],nums[point]
            runner +=1

    return point + 1

if __name__ == "__main__":
    arr = [1,1,2,2,2,3,3,3,3,3,4,4,4,4,4,5]
    final_arr = [1,2,3,4,5]
    k = move_unique_to_left(arr) 
    assert k == len(final_arr)
    for i in range(0 , k):
        assert arr[i] == final_arr[i]
    print("accepted")
    print(arr[0:k])

