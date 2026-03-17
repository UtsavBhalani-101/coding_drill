
def prob1():
    """invariant - for all the elements inside window, total sum <= 10, total elements <= 3"""

    # stream = [3,4,5,2,8]
    stream = [3, 3, 3, 10]
    window_sum = 0
    buffer = []

    for ele in stream:
        
        if ele > 10:
            continue

        while len(buffer) >= 3 or window_sum + ele > 10:
            window_sum -= buffer[0]
            buffer.pop(0)

        buffer.append(ele)
        window_sum += ele

        print(buffer)
        print(window_sum)

prob1()
