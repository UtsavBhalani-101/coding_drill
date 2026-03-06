
# ^ R1 _ processing a stream of integers

def prob():
    """invariant = the elements inside the batch are all non negative, 4 elements at max with max sum of 20"""
    
    stream = [3, 5, 2, 4, 6, 1, -1, 7, 8, 2, 3, 10, 5, -2, 4, 3, 2, 1]
    
    curr_batch = []
    batches = []

    for ele in stream:

        if ele < 0:
            curr_batch.clear()

        if ele >= 0:
            if len(curr_batch) < 4 and sum(curr_batch) + ele <= 20:
                curr_batch.append(ele)
            
            else:
                batches.append(curr_batch.copy())
                curr_batch.clear()
                if ele <= 20:
                    curr_batch.append(ele)

    batches.append(curr_batch.copy())
    
        # print(curr_batch)
    print(batches)
        

prob()