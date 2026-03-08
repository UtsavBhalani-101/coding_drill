
def prob():
    """invariant = the current window only contains 2 non decreasing, positive timestamps"""

    stream = [(0,'A'),
        (2,'B'),
        (3,'C'),
        (8,'D')]
    stream = [
        (10, "A"),
        (-5, "B"), # Illegal (Negative)
        (8, "C"),  # Illegal (Decreasing)
        (11, "D"), # Valid again
        (15, "E")  # New window
    ]

    window_size = 2
    batches = []
    curr_window = []
    curr_window_time = None
    prev_time = None

    for time, val in stream:
        
        # negative and non decreasing timestamps, ignore
        if prev_time is None:
            if time < 0:
                continue
        else:
            if time < 0 or (time < prev_time):
                continue

        if prev_time is None:
            # must be first entity
            curr_window.append((time, val))
            window_size -= 1
            curr_window_time = time + 5
            prev_time = time

        else: 
            if time <= curr_window_time:
                if window_size <= 2 and window_size >= 1:
                    curr_window.append((time, val))
                    window_size -= 1
                    prev_time = time

            else:
                batches.append(curr_window.copy())
                curr_window.clear()
                curr_window.append((time, val))
                window_size = 1
                curr_window_time = time + 5
                prev_time = time

    batches.append(curr_window.copy())

    print(batches)

prob()