
def prob():
    """invariant = the buffer only contains 3 positive elements in order"""

    stream = [10, 20, 30, 40, -5, 50, 60, 70, 80]

    batches = []
    buffer = []
        

    for ele in stream:
        if ele < 0:
            continue

        else:
            if len(buffer) < 3:
                buffer.append(ele)

            else:
                print("Buffer is full, current buffer saved to batch")
                batches.append(buffer.copy())
                buffer.clear()
                buffer.append(ele)

    batches.append(buffer.copy())

    print(batches)

prob()
