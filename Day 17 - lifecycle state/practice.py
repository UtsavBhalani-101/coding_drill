
def prob1():
    """invariant - the window only has total sum of 15 and total size of 4 without any consecutive
    even numbers """

    stream = [2, 4, 7, 3, 6, 8, 1, 5]
    # stream = [2, 3, 4, 5, 6]
    buffer = []
    last_ele = None
    window_sum = 0

    for ele in stream:

        if last_ele is None:
            if ele <= 15:
                buffer.append(ele)
                window_sum += ele
                last_ele = buffer[-1]
                print(buffer)
                continue

        if ele > 15:
            print(f"rejected {ele}, violated total sum constraint")
            continue

        while (len(buffer) >= 4) or (window_sum + ele > 15) or (((len(buffer) > 0) and (buffer[-1] % 2 == 0)) and (ele % 2 == 0)):
            if len(buffer) == 0:
                break
            popped = buffer.pop(0)
            window_sum -= popped

        buffer.append(ele)
        window_sum += ele
        last_ele = buffer[-1]

        print(buffer)

prob1()