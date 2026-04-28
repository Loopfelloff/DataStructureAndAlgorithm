def two_sum(nums , target):
    map = {}
    for index in range(0 , len(nums)):
        if(nums[index]) in map:
            return [index, map[nums[index]]]
        else:
            map[target-nums[index]] = index
    return []


if __name__ == "__main__":
    print(two_sum([1,2,3,4,5] , 9))
    
