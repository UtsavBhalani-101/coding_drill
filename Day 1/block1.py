
#? Given a string, count how many times each character appears.

def prob1(string: str):

    counter = dict()

    for i in string:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    return counter

# ? Given a string of integers separated by commas, compute the sum and mean.

def prob2():
    """
    input - string of numbers, output - sum and mean"""
    string = "10,20,30,40"
    var = list()
    count = 0
    sumation = 0
    mean = 0

    for i in range(len(string)):
        if string[i] != ',':
            """ it's a number"""

            var.append(string[i])
        if (string[i] == ',') or (i == (len(string) - 1)):
            """it's not a number but the prev chars are numbers"""
            full = ''
            for char in var:
                full += char
            
            int_val = int(full)
            count += 1

            sumation += int_val

            var.clear()

    print(sumation)
    mean = sumation / count
    print(mean)

    # this function assumes that the numbers are exactly after 1 comma and only integers between commas,
    # if there are more then one comma or any other non integer character like '/' then it breaks,
    # spaces are allowed 

# prob2()

# ? Write your own version of argmax.

def prob3():
    # arr = [3, 1, 9, 7, 9, 2]
    arr = [-2, -3, -1, -5]

    index = -1
    value = -1
    for i in range(len(arr)):
        """input a list, output = index and value
        require memory = yes why = to store and compare the current max"""

        if arr[i] > value:
            """ found a new max"""
            value = arr[i]
            index = i
    
    print(index)
    print(value)

    # this function assumes that the values are whole number, for negative numbers,
    # and value need to be set like the lowest possible value like in cpp INT_MIN

# prob3()

# ? Problem 4 — Line-by-Line File Processing (Reality Check)

def prob4():

    with open('data.txt', 'r') as f:
        file = f.readlines()

        count = 0
        mini = int(file[0])
        maxi = int(file[0])
        mean = 0
        total = 0


        for i in file:
            count += 1
            num = int(i)

            if num < mini:
                mini = num
            elif num > maxi:
                maxi = num
            
            total += num

        mean = total / count
    
    print(count)
    print(mini)
    print(maxi)
    print(mean)
prob4()



#! fixes 

def prob3_1():
    arr = [-2, -3, -1, -5]

    index = 0
    value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > value:
            index = i
            value = arr[i]

    print(index)
    print(value)

# prob3_1()

