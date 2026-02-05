
# ? Given a list of positive integers and an integer k, find the maximum length subarray whose sum is ≤ k.

def prob1():
    """ the numbers between left and right contains the largest subarray with sum <= k so far"""
    arr = [1, 2, 1, 0, 1, 1, 0]
    # arr = [1,2,100,3]
    k = 4

    left = 0
    current_sum = 0
    current_len = 0
    max_len = 0

    for right in range(len(arr)):

        current_sum += arr[right]
        
        while(current_sum > k):
            current_sum -= arr[left]
            left += 1

        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len

    return max_len

# print(prob1())

# ? Given a list of positive integers and a target, find the minimum length subarray whose sum ≥ target.

def prob2():
    """
    invariant = the numbers between left and right has a sum >= target
    """
    # arr = [2, 3, 1, 2, 4, 3]
    arr = [1,100,1]
    target = 7
    left = 0
    best_len = 0
    best_sum = 0
    current_len = 0
    current_sum = 0

    for right in range(len(arr)):
        current_sum += arr[right]
        current_len += 1

        while current_sum >= target:
            current_sum -= arr[left]
            current_len -= 1
            left += 1

            if current_sum >= target:
                if best_sum == 0:
                    best_sum = current_sum
                    best_len = current_len

                else:
                    best_sum = min(best_sum, current_sum)
                    best_len = min(best_len, current_len)

    print(best_len)
    print(best_sum)

# prob2()


# ? Return True if you can remove exactly one element to make the array strictly increasing.

def prob3():
    """ invariant = the current element is greater then the previous element so far"""

    # arr = [1, 2, 10, 5, 7]
    arr = [2,2,2]
    dips = []

    for i in range(1, len(arr)):
        left = arr[i-1]
        if arr[i] > left:
            continue

        elif i == 1 and arr[i] < left:
            dips.append(left)

        elif arr[i] > arr[i-2] and arr[i] < left:
            dips.append(left)

        else:
            dips.append(left)

    if len(dips) <= 1:
        print("True")
    else:
        print("False")

    print(dips)
# prob3()

# ? Return True if s2 is a rotation of s1.

def prob3():
    """
    
    """

    # s1 = "abcd"
    # s2 = "cdab"
    s1 = "abc"
    s2 = "ab"