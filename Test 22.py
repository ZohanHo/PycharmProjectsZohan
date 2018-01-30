def get_int (msg):
    while True:
        try:
            i = input (int(msg))
            return i
        except  ValueError as err:
            print(err)
            break
get_int("g")