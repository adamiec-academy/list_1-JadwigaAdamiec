def envelope(n):
    print("*" * (2*n +1))
    for i in range(n-1):
        print ("*" + " " * i + "*" + " " * (2*n-3-2*i) + "*" + " " * i + "*")
    print("*" + " " * (n-1) + "*" + " " * (n-1) + "*")
    for j in range(n-1):
        print ("*" + " " * (n-j-2) + "*" + " " * (2*n-2*(n-j)+1) + "*" + " " * (n-j-2) + "*")
    print("*" * (2*n +1))
