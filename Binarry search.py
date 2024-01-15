def myarray(numbers, key):
    #We define the start and finish for an array. The array should be sorted.
    St=0
    Ed =len(numbers)-1
    # we run until we have found the exact key or value. if key== mid then it is printed.
    #if key is < mid then wwe add one to the mid so it is going to be our start
    # if key is > mid then we just simply minus one from mid so we determine our end for that.
    while St<=Ed:
        mid= (St+Ed)//2
        if numbers[mid]==key:
            return mid
        if numbers[mid]<key:
            St=mid+1
        else:
            Ed=mid-1
    return None

Muarray=[2, 4,10,11, 18,19, 25, 29, 30, 38, 45, 85, 195, 199, 295, 500, 656, 768, 897, 987, 1000]
key=656
result= myarray(Muarray, key)
if result is not None:
    print(f'The binary search option for {key} is at index {result}')
else:
    print(f'The binary search option for {key} is not found')
