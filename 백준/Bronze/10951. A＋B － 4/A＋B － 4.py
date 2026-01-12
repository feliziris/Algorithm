while True:
    try:
        input_ = input()
        A, B = input_.split()

        if A.isdigit() and B.isdigit():
            print(int(A) + int(B))
    except:
        break