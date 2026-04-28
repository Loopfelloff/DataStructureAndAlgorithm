def sum_of_array(arr):
    if(len(arr) != 1):
        return arr[0] + sum_of_array(arr[1:])
    else :
        return arr[0]

print(sum_of_array(arr=[1,1,1,1]))
