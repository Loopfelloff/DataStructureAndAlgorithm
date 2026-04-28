# for reversing the strings.

# you can simply call array.reverse() and that solves the problem

# however using two pointer solution

def reverse_string(string):
    first , last = 0 , len(string)-1
    while first < last : 
        string[first] , string[last] = string[last] , string[first]
        first +=1
        last -=1

if __name__ == '__main__':
    arr = list('loopfelloff')
    reverse_string(arr)
    print(arr)

