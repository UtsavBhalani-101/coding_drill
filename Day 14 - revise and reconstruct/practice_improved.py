
# ^ thermal monitor

def prob():

    """invariant = only increasing timestamps with temperature <= 100 are allowed"""

    stream = [
        (10, 85),
        (15, 90),
        (14, 92),  # Network delay
        (20, 105), # Meltdown
        (25, 80)   # Post-meltdown
    ]
    is_alive = True
    batch = []
    prev_time = None

    for curr_time, curr_temp in stream:

        # system must be live 
        if not is_alive:
            break

        if prev_time == None:
            # this must be the first index
            if curr_temp <= 100:
                batch.append((curr_time, curr_temp))
                prev_time = curr_time

        else:
            if curr_time > prev_time:
                if curr_temp <= 100:
                    batch.append((curr_time, curr_temp))
                    prev_time = curr_time
                else:
                    print("CRITICAL SHUTDOWN")
                    is_alive = False

    print(batch)

    

prob()