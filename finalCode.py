for count in range(1, 51):
    if count % 5 == 0:
        print("HiFive")
    elif count % 2 == 0:
        print("HiTwo")
    elif count % 3 == 0 or count % 7 == 0:
        print("HiThreeOrSeven")
    else:
        print(count)