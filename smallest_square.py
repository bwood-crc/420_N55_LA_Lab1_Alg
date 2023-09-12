def find_next_square(num):
    n = 0
    while 2 ** n < num:
        n += 1
    return 2 ** n


print(find_next_square(33))
