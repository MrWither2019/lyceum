A = input().split()
Ma = -99e100
Mi = 99e100
for i in range(len(A)):
    if int(A[i]) > Ma:
        Ma = int(A[i])
for i in range(len(A)):
    if int(A[i]) < Mi:
        Mi = int(A[i])
print(Mi)
print(Ma)
