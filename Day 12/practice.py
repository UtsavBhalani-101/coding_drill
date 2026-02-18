
def nuclear():
    """invariant - buffer contains no negative numbers with a max size of 5 and if the buffer is 
                    full, anything else encountered is error"""
    # arr = [10, 20, 30, 40, 50, 60]
    arr = [1, 2, 3, 4, 5, 6, -1, 8]
    buffer = []
    size = 0

    for i in arr:
        if size < 5:
            if i >= 0:
                buffer.append(i)
                size += 1
            
            else:
                raise BufferError(f"Buffer is not full but can't reject the valid elements in buffer")

        elif size == 5:
            if i >= 0:
                raise BufferError(f"Buffer is full, can't add new element {i} and remove an element from the buffer")
            else:
                raise BufferError(f"Buffer is full, can't reject element {i} and clear the buffer")
            
    print(buffer)

# nuclear()            


def whistleblower():
    """invariant - buffer contains no negative numbers with a max size of 5 and if buffer is full 
    and encountered valid number, shout(print) and save"""
    # arr = [10, 20, 30, 40, 50, 60]
    arr = [1, 2, 3, 4, 5, 6, -1, 8]
    buffer = []
    size = 0
    extra_buffer = []

    for i in arr:
        if size < 5:
            if i > 0:
                buffer.append(i)
                size += 1

        elif size == 5:
            if i > 0:
                print(f"Buffer is full, transfering the first element {buffer[0]} to extra buffer")
                extra_buffer.append(buffer[0])
                buffer.pop(0)
                buffer.append(i)
                print(buffer)
                print(extra_buffer)


whistleblower()