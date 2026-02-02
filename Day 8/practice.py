
# ? Given a list of positive integers and an integer k, find the maximum length subarray whose sum is ≤ k.

def prob1():
    """ the numbers between left and right contains the largest subarray with sum <= k so far"""
    # arr = [1, 2, 1, 0, 1, 1, 0]
    arr = [5, 5, 1, 1, 1, 5]
    k = 3
    left = 0
    current_nums = []
    current_sum = 0
    
    for right in range(len(arr)):

        if left == 0 and right == 0 and arr[right] > k:
            left += 1


        elif (current_sum + arr[right]) <= k:
            current_sum += arr[right]
            current_nums.append(arr[right])

        elif (current_sum + arr[right]) > k and (current_sum - arr[left] + arr[right]) < k:
            current_sum -= arr[left]
            current_nums.remove(arr[left])
            left += 1

            current_sum += arr[right]
            current_nums.append(arr[right])

        print(current_nums, current_sum)

# prob1()

# ? Given a list of integers, return the first index where the running sum becomes negative.

def prob2():
    """the cum_sum calculates the +ve cumilative sum so far"""
    # arr = [3, -4, 2, -3, -1, 7]
    arr = [5, -5, 2]
    cum_sum = 0

    for i in range(len(arr)):
        if (cum_sum + arr[i] )>= 0:
            cum_sum += arr[i]

        elif (cum_sum + arr[i]) < 0:
            return i
        
    return -1

# print(prob2())

# ? Return True if you can remove exactly one element to make the array strictly increasing.

def prob3():
    """ invariant = remove the element just before the dip"""

    # arr = [1, 2, 10, 5, 7]
    arr = [2,2,2]
    dips = 0

    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            dips += 1
            if arr[i] > arr[i-2] and arr[i+1] > arr[i]:
                continue
            else:
                dips += 1


    if dips <= 1:
        return True
    else:
        return False

print(prob3())