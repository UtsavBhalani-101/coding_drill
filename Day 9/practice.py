
# ? Given an array of integers and an integer k, return the 
# ? length of the longest contiguous subarray that contains exactly k distinct elements.

def prob1():
    """invariant: the element inside the window, satisfies the constraint (variety = k)"""
    arr = [1, 2, 1, 2, 3]
    k = 2
    left = 0
    current = []
    best = []
    current_k = 0

    for right in range(len(arr)):

        if arr[right] in current:
            current.append(arr[right])

        elif arr[right] not in current:
            current.append(arr[right])
            current_k += 1


        while current_k > k:
            current.remove(arr[left])
            left += 1

        best = max(current, best)

        print(current)
        print("best", best)

# prob1()        

# ? Given an array, return the first index where the element is greater than
# ? the element immediately to its left, after the array has been decreasing so far.

def prob2():
    """ invariant: all the elements before the current index are valid"""
    arr = [9, 7, 5, 3, 6, 2]
    # arr = [1]

    for i in range(1, len(arr)):
        if arr[i-1] < arr[i]:
            return i
        
    return -1
        
# print(prob2())

# this was too easy, I checked for 7 different edge cases and passed all, is it really correct ?

# ? Given a binary array, 
# ? return the minimum number of swaps required to make it alternating (0101… or 1010…).

def prob3():
    """invariant: all the mismatched element so far are counted"""
    # arr = [1, 0, 1, 0, 1, 0]
    arr = [0, 0, 1, 1]
    ones = 0
    zeros = 0
    mismatch = 0

    for i in arr:
        if i == 0:
            zeros += 1
        else:
            ones += 1

    if abs(ones - zeros) > 1:
        return -1
    elif abs(zeros - ones) > 1:
        return -1

    if ones >= zeros:
        odd = 0
        even = 1
    elif zeros >= ones:
        odd = 1
        even = 0


    for ele in range(len(arr)):
        if ele % 2 != 0:
            if arr[ele] != odd:
                mismatch += 1

        elif ele % 2 == 0:
            if arr[ele] != even:
                mismatch += 1

    return mismatch // 2


# print(prob3())


# ? Given a stream of integers, return the first 
# ? index i such that: arr[i-1] < arr[i] > arr[i+1]

def prob4():
    """invariant: the current number is not greater then it's neighbors"""
    # arr = [1, 2, 3, 1, 0]
    arr = [5,1,5]

    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return i
        
    return -1
        
print(prob4())
        
