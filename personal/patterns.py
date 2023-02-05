def pattern(N,ele):
    for i in range(1,2*N):
        if i<=N:
            n=i
        else:
            n=2*N - i
        spaces=2*N - 2*n
        print(ele*n+" "*spaces+" "*spaces+ele*n)

pattern(6,"* ")

def block(N):
    for i in range(2*N-1):
        col = ""
        till = N-i
        