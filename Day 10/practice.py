

#! invariant = the bucket only takes on +ve no.
"""
invariant = the bucket only takes on positive numbers until sum <= 100
"""

def prob():
    # values = [20, 50, 40, 10, -5, 30, 80]
    values = [10, 20, 30, -1, 50, 60, -99]
    batches = {}
    current = []
    total = 0
    name = 1
    
    for ele in values:
        if (ele >= 0) and (total + ele <= 100):
            current.append(ele)
            total += ele

        elif ele < 0:
            current.clear()
            total = 0

        elif (ele >= 0) and (total + ele > 100):
            current.append(ele)
            total += ele
            batches[f'batch_{name}'] = list(current)
            name += 1
            current.clear()
            total = 0

    print(batches)

prob()

"""
1. the state - total and current. current and total both changes
2. once the loop starts the invariant must never break """