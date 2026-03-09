def prob2():
    """invariant - the batch only contains non -ve, ordered, with at max sum of 15 with no greater then 4 elements"""

    # stream = [5, 7, 3, 9, 2, 6, -1, 4, 8, 1]
    stream = [10, -5, -2, 4]
    batch = []
    final_batch = []
    batch_len = 0
    batch_sum = 0

    for ele in stream:
        if ele < 0:
            print("-ve number appeared")
            batch.clear()
            batch_len = 0
            batch_sum = 0
            continue

        else:
            if batch_len < 4:
                if batch_sum + ele <= 15:
                    batch.append(ele)
                    batch_len += 1
                    batch_sum += ele
                    print(batch)
                
                else:
                    print(f"Batch has reached total limit, can't accept {ele}")
                    final_batch.append(batch.copy())
                    batch.clear()
                    batch_sum = 0
                    batch_len = 0

                    if batch_sum + ele <= 15:
                        batch.append(ele)
                        batch_len = 1
                        batch_sum = ele

            else:
                print(f"Batch size limit reached, can't accept {ele}")
                final_batch.append(batch.copy())
                batch.clear()
                batch_sum = 0
                batch_len = 0

                if batch_sum + ele <= 15:
                    batch.append(ele)
                    batch_len = 1
                    batch_sum = ele

    final_batch.append(batch.copy())
    print(final_batch)

# prob2()

def prob3():
    """invariant - the batch only contains non -ve, ordered, with at max sum of 15 with no greater then 4 elements"""

    # stream = [5, 7, 3, 9, 2, 6, -1, 4, 8, 1]
    stream = [10, -5, -2, 4]
    batch = []
    final_batch = []
    batch_len = 0
    batch_sum = 0

    for ele in stream:
        if ele < 0:
            print("-ve number appeared")
            batch.clear()
            batch_len = 0
            batch_sum = 0
            continue

        else:
            if batch_len < 4 and batch_sum + ele <= 15:
                batch.append(ele)
                batch_len += 1
                batch_sum += ele
                print(batch)

            else:
                print(f"Batch size limit reached, can't accept {ele}")
                final_batch.append(batch.copy())
                batch.clear()
                batch_sum = 0
                batch_len = 0

                if batch_sum + ele <= 15:
                    batch.append(ele)
                    batch_len = 1
                    batch_sum = ele

    final_batch.append(batch.copy())
    print(final_batch)

prob3()