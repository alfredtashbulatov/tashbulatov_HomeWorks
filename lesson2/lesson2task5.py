def month_to_season(n):
        s = n
        if s == 12 or s == 1 or s ==2:
            print("Winter")
        elif s == 3 or s == 4 or s == 5:
            print("Spring")
        elif s == 6 or s == 7 or s == 8:
            print("Summer")
        elif s == 9 or s == 10 or s == 11:
            print("Fall")
        else:
            print(s)

month_to_season(10)
    

