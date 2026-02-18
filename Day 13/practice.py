
def prob():
    """invariant - the request buffer contains at max 3 request with (timestamp, request_id) format
                    with valid timestamps (positive and non decreasing) if 3+ requests then show error"""
    
    # test_set_1 = {
    #     1: "A",
    #     4: "B",
    #     8: "C",
    #     12: "D"
    # }
    test_set_1 = {
        0: "A",
        -5: "B",
        2: "C"
    }

    curr_buffer = []
    buffer = {}
    size = 0
    current_time_limit = 0


    for index, (time, req) in enumerate(test_set_1.items()):
        if index == 0:
            if time >= 0:
                curr_buffer.append((time, req))
                size += 1
                current_time_limit = time + 10
            else:
                print("No negative timestamps allowed")

        else:
            if time >= 0:
                if list(test_set_1.keys())[index] >= list(test_set_1.keys())[index-1]:
                    if time <= current_time_limit:
                        if size < 3:
                            curr_buffer.append((time, req))
                            size += 1
                        else:
                            print(f"The buffer is full for these 10 mins, can't accept {(time, req)}")

                    elif time > current_time_limit:
                        buffer.update(curr_buffer)
                        curr_buffer.clear()
                        curr_buffer.append((time, req))
                        size = 1
                        current_time_limit = time + 10
                else:
                    print("No decreasing timestamps allowed")
            else:
                print("No negative timestamps allowed")

        print(curr_buffer)
        print(current_time_limit)
        # print(size)
        print(buffer)

# prob()


def prob2():
    """invariant - the request buffer contains at max 3 request with (timestamp, request_id) format
                    with valid timestamps (positive and non decreasing) if 3+ requests then show error"""
    
    requests = [
        (1, "A"),
        (4, "B"),
        (8, "C"),
        (12, "D")
    ]
    # test_set_1 = {
    #     0: "A",
    #     -5: "B",
    #     2: "C"
    # }

    size = 0
    current_time_limit = 0
    prev_time = None


    for time, req in requests:
        if prev_time is None:
            if time >= 0:
                size += 1
                current_time_limit = time + 10
                
        else:
            if time >= 0:
                if time >= prev_time:
                    if time <= current_time_limit:
                        if size < 3:
                            size += 1
                        else:
                            print(f"The buffer is full for these 10 mins, can't accept {(time, req)}")
                    elif time > current_time_limit:
                        size = 1
                        current_time_limit = time + 10

        prev_time = time

        print(current_time_limit)
        # print(size)


prob2()