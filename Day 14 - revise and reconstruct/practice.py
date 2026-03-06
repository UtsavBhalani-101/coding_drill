
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

    for i in range(len(stream)):

        if is_alive:

            if i == 0:
                if stream[i][1] <= 100:
                    batch.append(stream[i])
                    continue
                
            prev_timestamp = stream[i-1][0]
            current_timestamp = stream[i][0]
            current_temp = stream[i][1]

            if prev_timestamp < current_timestamp:
                if current_temp <= 100:
                    batch.append(stream[i])

                else:
                    print("CRITICAL SHUTDOWN")
                    is_alive = 0
            else:
                continue

        else:
            break

    # print(batch)
        

prob()