for j in range (1,11,1):
    for jj in range (10,j,-1):
        print(" ",end=" ")
    for jjj in range(1,j,1):
        print("*",end=" ")
    for jjjj in range (1,j,1):
        print("*",end=" ")
    print()
for a in range (1,11,1):
    for aa in range (1,a,1):
        print(" ",end=" ")
    for aaa in range(10,a,-1):
        print("*", end=" ")
    for aaaa in range(10,a,-1):
        print("*", end=" ")
    print()