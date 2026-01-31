
# ? Given a list of integers, find the length of the longest contiguous strictly increasing subarray.

def prob1():
    arr = [1, 2, 2, 3, 4, 1, 2, 3]
    best = 0
    current = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current += 1

        else:
            current = 1

        if current > best:
            best = current

    print(best)

# prob1()

# ? Given a list of integers, find the smallest positive integer missing.

def prob2():
    nums = [1,2,3,7,8,9,11,12]
    count = 1
    flag = False

    while True:
        for i in nums:
            if i == count:
                flag = True

        if flag == True:
            count += 1
            flag = False
            continue

        else:
            break
    
    
    print(count)
            
# prob2()

# ? Move all negative numbers to the front, positives to the back, preserving relative order.

def prob3():
    nums = [1, -2, 3, -4, -1, 5]
    # nums = [1,9,-3,-4,4,-6]
    pos = nums[0]
    neg = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0 and nums[i-1] >= 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]

        elif nums[i] >= 0 and nums[i] < 0:
            nums[i], nums[i-1] = nums[i-1], nums[i]

    print(nums)
prob3()

# ? Find the element that appears more than n/2 times.

def prob4():
    nums = [2, 2, 1, 1, 1, 2, 2]
    current = nums[0]
    count = 1
    final = 0

    for i in range(1, len(nums)):

        if count == 0 and current != nums[i]:
            current = nums[i]
            count = 1

        elif current == nums[i]:
            count += 1
        else:
            count -= 1

        if count > (len(nums) / 2) and count > final:
            final = current
        
    print(current)

# prob4()