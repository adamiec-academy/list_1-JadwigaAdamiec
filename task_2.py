
def chess_board(n,k):
    for j in range(n):
        for i in range(k):
            print((" " * k + "#" * k) * n)
        for i in range(k):
            print(("#" * k + " " * k) * n)
    pass
