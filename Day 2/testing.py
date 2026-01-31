def prob4():
    arr = [2, 4, 6, 8]
    mean = 0
    total = 0

    for i in range(len(arr)):
        total += arr[i+1]

        mean = total / (i+1)
        print(mean)

prob4()