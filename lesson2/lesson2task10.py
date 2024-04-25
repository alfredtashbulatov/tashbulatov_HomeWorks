def bank(x, y):
    for i in range(1, y + 1):
        count = x + (x / 10)
        x = count 
    print(round(x, 4))

bank(1000, 5)    