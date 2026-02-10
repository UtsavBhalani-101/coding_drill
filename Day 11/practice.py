
def prob():
    """invariant = the batch contains positive numbers with a max size of 5 and max sum of 50"""
    # arr = [10, -5, 20, -100, 5]
    arr = [10, 60, 5]

    batches = {}
    current = []
    total = 0
    name = 0

    for i in arr:

        if (i >= 0) and (i < 50):
            if ((total + i <= 50) and (len(current) + 1 <= 5)):
                current.append(i)
                total += i


            elif (total + i > 50) or (len(current) + 1 > 5):
                batches[f'batch_{name}'] = list(current)
                name += 1
                current.clear()
                current.append(i)
                total = i
            
               
        # print(current)
    
    if len(current) <= 5 and total <= 50:
        batches[f'batch_{name}'] = list(current)

    print(batches)

prob()

"""
1. all 3 are safety invariants 
2. if total + i > 50 don't allow 
3. if size + 1 > 50 then save the current batch and reset the batch and total"""

"""so here's my understanding for this one. The invariants are hard constraints that MUST be protected at all costs, how to do that ? you have guards. a guard is just a safety mechanism that protects one invariant from violating. the guard either permit or not but some invariants are required a state change when broken or before broken to save the invariant, this action is the safety mechanism that is encoded into the transitions. some invaraints do not need state changes to protect them, these are simple ones but the others are a little complex ones"""

""" there does exists soft constraints but not in this one and they don't have a safety net but a cost of breaking """