
# ? problem 1 - Reverse a list in place.

def prob1():
    arr = [1, 2, 3, 4, 5]
    arr2 = [1,2,3,4,5,6,7,8]

    if len(arr) % 2 != 0:
        """odd"""
        for ind in range(len(arr)):

            start = ind
            end = len(arr) - start - 1

            if start == end:
                break
            temp = 0

            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp

        # print(arr)

    if len(arr2) % 2 == 0:
        """even"""
        range_val = int(len(arr2) / 2)
        for ind in range(range_val):
            start = ind
            end = len(arr2) - start - 1

            temp = 0
            temp = arr2[start]
            arr2[start] = arr2[end]
            arr2[end] = temp

        print(arr2)
    # INVARIANTS: the start and end points to first and last position of CURRENT iteration

# prob1()

#? Return True if the string is a palindrome.

def prob2():
    string = "abcba"
    char = list(string)

    if len(char) % 2 != 0:
        """odd"""
        for ind in range(len(char)):
            start = ind
            end = len(char) - start - 1

            if start == end:
                break
            
            temp = ""
            temp = char[start]
            char[start] = char[end]
            char[end] = temp

    elif len(string) % 2 == 0:
        """even"""
        range_val = int(len(string) / 2)
        for ind in range(range_val):
            start = ind
            end = len(char) - start - 1
            
            temp = ""
            temp = char[start]
            char[start] = char[end]
            char[end] = temp
    
    newstr = ""
    for i in char:
        newstr += i

    if newstr == string:
        print("Is palindrome")
    else:
        print("Is not palindrome")

    # both code blocks works for both cases
    # INVARIANTS: start and end keep track of CURRENT INDEX'S start & end

# prob2()

# ? Move all zeros to the end without changing order of non-zeros. 

def prob3():
    inp = [0, 1, 0, 3, 12]
    for i in range(len(inp)):
        if inp[i] == 0:
                
                for j in range(i, len(inp)):
                    if (j+1) <= (len(inp) - 1):
                        
                        temp = 0
                        temp = inp[j]
                        inp[j] = inp[j+1]
                        inp[j+1] = temp


    print(inp)
# prob3()

# ? Given a list and a target, return the first pair of indices whose values sum to target.

def prob4():
    arr = [2, 7, 11, 15]
    target = 9

    rem = 0
    flag = False
    for i in range(len(arr)):
        if (arr[i] <= target) and (target - arr[i] >= 0):
            rem = target - arr[i]

            for j in range(i, len(arr)):
                if arr[j] == rem:
                    print("pair found")
                    print(i, j)
                    flag = True
                    break

    if flag == False:
        print("pair not found")
                    
prob4()


def prob5_1():
    inp = [0, 1, 0, 3, 12]
    for i in range(len(inp)):
        if inp[i] == 0:
                
                for j in range(len(inp)):
                    if (j+1) <= (len(inp) - 1):
                        
                        temp = 0
                        temp = inp[j]
                        inp[j] = inp[j+1]
                        inp[j+1] = temp


    print(inp)

# INVARIANT = the inner loop only runs if it encounters 0 and takes THAT INDEX'S 0 to the end
# breaking encountering = will do the opposite
# breaking inner loop range = will result in something expected, idk 

# prob5_1()

def prob5_2():
    arr = [3, 56, 4, 2, 6]
    target = 9

    rem = 0
    flag = False
    for i in range(len(arr)):
        if (i < target) and (target - arr[i] > 0):
            rem = target - arr[i]

            for j in range(i, len(arr)):
                if arr[j] == rem:
                    print("pair found")
                    print(i, j)
                    flag = True
                    break

    if flag == False:
        print("pair not found")

# INVARIANTS: It finds the first num < target and second == remainder, from the rest 
# if broke inner loop range: it will give 2 same pairs like 0,3 and 3,0

# prob5_2()