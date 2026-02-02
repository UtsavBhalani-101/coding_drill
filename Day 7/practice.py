
# ? Given a list, find the length of the longest contiguous
# ? prefix where the sequence is non-decreasing allowing at most one drop.

def prob1():
    """
    invariant = the count denotes the count of numbers that follow the rule and drops denote
                the number of times ther's a drop SO FAR"""
    series = [1, 2, 5, 3, 4, 6]
    count = 1
    drops = 1

    for i in range(1, len(series)):

        if series[i] >= series[i-1]:
            count += 1
            continue

        elif series[i] < series[i-1] and drops != 0: 
            count += 1
            drops = 0

        elif series[i] < series[i-1] and drops == 0:
            break

    print(count)

prob1()

# ? Given a list of positive integers and a target, find the minimum length subarray whose sum ≥ target.

def prob2():
    """
    invariant = the current_sum holds the sum so far and when the condition is 
                satisfied, it's compared with the best_sum
    """
    arr = [2, 3, 1, 2, 4, 3]
    target = 7
    current_list = []
    current_sum = 0
    best_sum = 0
    best_list = []

    for i in arr:
        current_sum += i
        current_list.append(i)
        # print(current_sum)
        # print(current_list)

        if current_sum >= target:
            if best_sum == 0:
                best_sum = current_sum
                best_list = current_list

            elif current_sum <= best_sum:
                best_sum = current_sum
                best_list = current_list

            current_sum = 0
            current_list = []


    print(best_sum, best_list)
    print(len(best_list))
# prob2()

# ? Return True if s2 is a rotation of s1.

def prob3():
    """

    I am assuming that both strings are of same length

    if they are actual rotations of each other, then the only difference between them is
                the position at which each string starts.

    invaraint = we first find the position at which both are same and start checking
                each char SO FAR, if any mismatch - not a rotation
                
                so far doesn't really fits here btw (according to me)"""

    # s1 = "abcd"
    # s2 = "cdab"
    s1 = "abc"
    s2 = "ab"
    flag = True

    index = 0

    if len(s1) != len(s2):
        return "String's don't match in length"
    
    while flag:
        if s1[0] == s2[index]:
            flag = False

        else:
            index += 1


    for i in range(len(s1)):

        new_ind = (index + i) % 4
        
        if s1[i] != s2[new_ind]:
            return "Not a rotation"

    
    if index == 0:
        return "they are same"
    return "they are rotation"

# print(prob3())

# ^ this only checks for rotation in one direction

# ? Given a stream of integers, find the second largest element.
def prob4():
    """
    invariant = the larget holds the largest So far and second largest holds the second largest so far"""
    # nums = [5, 1, 4, 2, 3]
    nums = [-1, -2]
    largest = nums[0]
    second = nums[1]

    for i in range(1, len(nums)):
        if nums[i] > largest:
            second = largest
            largest = nums[i]

        elif nums[i] > second and nums[i] < largest:
            second = nums[i]

    print(largest, second)

# prob4()


def prob5():
    """
    invariant = the current_sum holds the sum so far and when the condition is 
                satisfied, it's compared with the best_sum
    """
    arr = [1,1,1,1,1,1]
    target = 11
    current_list = []
    current_sum = 0
    best_sum = 0
    best_list = []

    for i in arr:
        current_sum += i
        current_list.append(i)
        # print(current_sum)
        # print(current_list)

        if current_sum >= target:
            if best_sum == 0:
                best_sum = current_sum
                best_list = current_list

            elif current_sum < best_sum:
                best_sum = current_sum
                best_list = current_list

            current_sum = 0
            current_list = []

    print("_________")
    print(best_sum, best_list)
    print(len(best_list))

# prob5()

#^ the elif still works, so it might be redandant 


