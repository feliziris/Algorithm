while True:
    N = input()
    if N.isdigit():
        N = int(N)
        break

for i in range(N):
    input_ = input()
    A, B = input_.split()
    print(int(A)+int(B))