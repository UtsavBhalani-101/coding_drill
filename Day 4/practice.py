
# ? Given a string, find the **length of the longest contiguous run** of the same character.

def prob1():
    text = "aaabbccccddeee"
    current = 0
    best = 0

    for i in range(len(text)):
        if current == 0:
            current_char = text[i]
            current += 1

        elif current_char == text[i]:
            current += 1
        
        elif current_char != text[i]:
            if best < current:
                best = current
            current = 1
            current_char = text[i]

    print(current)

prob1()

def prob1_1():
    text = "aaabbccccddeee"
    current = 0
    best = 0

    for i in range(len(text)):
        if current == 0:
            current += 1
            current_char = text[i]

        elif current_char == text[i]:
            current += 1

        else:
            current = 1
            current_char = text[i]

        if current > best:
            best = current 

    print(best)

# prob1_1()


# ? Return `True` if the list is strictly increasing, else `False`.

def prob2():
    inc = [1, 2, 3, 5]
    ninc = [1, 2, 2, 3]

    for i in range(1, len(inc)):
        if inc[i-1] >= inc[i]:
            return False
            
    return True

# print(prob2())

# ? Given daily prices, find the **maximum profit** from one buy and one sell.

def prob3():
    prices = [7, 1, 5, 3, 6, 4]

    min_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] < min_price:
           min_price = prices[i] 

        else:
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
        
            
    print(profit)
# prob3()


# ? Remove adjacent duplicates until none remain.

def prob4():
    text = "abbaca"
    stack = []

    for i in range(len(text)):
        if len(stack) == 0:
            stack.append(text[i])

        elif stack[-1] == text[i]:
            stack.pop()

        else:
            stack.append(text[i]) 

    print(stack)
# prob4()


def prob5_1():
    prices = [7, 1, 5, 3, 6, 4]

    min_price = prices[0]
    profit = 0

    for i in range(1, len(prices)):

        if prices[i] < min_price:
            min_price = prices[i] 

        else:
            if prices[i] - min_price < profit:
                profit = prices[i] - min_price
        
            
    print(min_price, profit)

# prob5_1()

"""
test1:
removing first if cond. --- the min prices updates every time

test2:
reversing first if cond. --- then min price becomes max price

test3:
removing else. --- it works, bcoz now we are checking both every time and when min price is 
updated, profit = 0

test4:
removing second if --- the profit is last value - min price 

test5:
reversing second if cond. --- the profit is 0 bcoz now the profit wants to become negative 
if possible but for that either the min price should be higher or the prices[i] < min price


the if -- checks if the current price a good candidate for min price
the else -- if the price is not good candidate then is the profit high enough 
the if -- checks for the profit, if the current profit the highest 
"""

def prob5_2():
    text = "abbaca"
    stack = []

    for i in range(len(text)):
        if len(stack) == 0:
            stack.append(text[i])

        elif stack[-1] == text[i]:
            stack.pop()

        # else:
        stack.append(text[i]) 

    print(stack)

prob5_2()

"""
test1
removing first if --- no output bcoz the char added then in the next condition it matches and gets removed

test2
reverse first if --- error - index out of range

test3
removing elif --- empty bcoz it adds and removed in each iter

test4
reversing elif --- empty bcoz it removes every time it's not same 

test5
removing else --- all ele bcoz all are added  


the first if -- for first index and list out of range error 
the elif -- the main checker, if same then pop 
the else -- reverse of elif checker, if not popped then add
"""