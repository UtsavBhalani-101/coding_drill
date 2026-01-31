
# ? Given a list of integers, find the smallest positive integer missing.

def prob2():
    nums = [1,2,3,7,8,9,11,12]
    smallest = 1
    flag = False
    
    for i in range(1, max(nums)+1):
        smallest = i
        for j in nums:
            if smallest == j:
                print("found a match for ", smallest)
                flag = True

        if flag == False:
            print("No match found, likely smallest")
            return smallest
        
        else:
            flag = False
            
# print(prob2())

# ? Move all negative numbers to the front, positives to the back, preserving relative order.

def prob3():
    nums = [1, -2, 3, -4, -1, 5]
    temp = []
    for i in nums:
        if i < 0:
            temp.append(i)
            print(temp)

# prob3()

# ? Find the element that appears more than n/2 times.

def prob4():
    nums = [2, 2, 1, 1, 1, 2, 2]
    count = 1
    candidate = nums[0]

    for i in range(1, len(nums)):
        if nums[i] != candidate and count != 0:
            count -= 1

        if nums[i] != candidate and count == 0:
            count = 1
            candidate = nums[i]

        elif nums[i] == candidate:
            count += 1
        
    print(candidate)
    print(count)

prob4()