
# ? Given a list, return a new list with duplicates removed while preserving order.

def prob1():
    """ remove duplicates
    input = list with duplicates
    output = list without duplicates
    need state = yes"""
    arr = [3, 5, 3, 7, 5, 9, 3]

    newarr = []

    for i in arr:
        """I need only value"""
        if i not in newarr:
            newarr.append(i)
        
    print(newarr)

# prob1()

def prob1_1():
    arr = [3, 5, 3, 5, 7, 5, 9, 3]
    newarr = []
    flag = 0
    # flag is used as a switch to denote existence

    for i in arr:
        for j in newarr:
            if i == j:
                flag = 1
            
        if flag == 0:
            newarr.append(i)
        flag = 0

    print(newarr)

# prob1_1()

""" if the default condition is set to 1, and matching is += 1, then also works"""

# ? Given a string, return the first character that appears exactly once.

def prob2():
    """input = string
    output = a non duplicated character
    state req = yep
    """

    string = "aabbccdeeff"
    flag = 0
    duplicates = []
    unique = []

    for i in range(len(string)):

        if string[i] in duplicates:
            continue

        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                duplicates.append(string[i])
                flag = 1
                break
            
        if flag == 0:
            unique.append(string[i])
        flag = 0

    print(unique)

# prob2()

# if flag removed = duplicates remains same, unique behaves like a set
# bcoz all the element will go in unique but those who are duplicates will go to duplicates
# and if the unique is inside the nested loop then every char repeats len(string) times  


# ? pattern 

def prob3():
    n = 5

    for i in range(1, n+1):
        print("*" * i)

    for j in range(n-1, 0, -1):
        print("*" * j)

    """I think I cheated a little with this string x number trick"""

# prob3()

def prob3_1():
    n = 5

    for i in range(1, n+1):
        for j in range(i):
            print('*', end='')

        print()

    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end='')
        print()

# prob3_1()

# changing the range from (1, i+1) to just (i) won't have any effect as the nested loop,
# is used only for printing and number is not required
# the ranges are soft ranges, if they are replaced with just n or i,
# then there would be empty spaces before and after the pattern. - due to 0 or -ve numbers

# ? Given a list of numbers, print the running mean after each element.

def prob4():
    arr = [2, 4, 6, 8]
    mean = 0
    total = 0

    for i in range(1, len(arr)+1):
        total += arr[i-1]

        mean = total / i
        print(mean)
# prob4()

# the total is used to keep track of all the previous numbers 
# the i is taken as range and not as number as we also want continous mean with increasing denom
# and also division with zero if used just len(arr)
# either total or mean, one of them needs to have a number to work with denom
# if mean is plain then we have to supply indexes + 1 as denom to avoid division with 0
