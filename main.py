import random
from time import perf_counter
def CountingSort(L,n):
    output=[0]*n
    max=maxim(L,n)
    count=[0]*(max+1)
    for i in range(n):
        count[L[i]]+=1
    for i in range(1,max+1):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        output[count[L[i]]-1]=L[i]
        count[L[i]]-=1
        i-=1
    for i in range(n):
        L[i]=output[i]
def InsertionSort(L,n):
    for i in range(1,n):
        key=L[i]
        j=i-1
        while key<L[j] and j>=0:
            L[j+1]=L[j]
            j-=1
        L[j+1]=key
def mergeSort(L,n):
    if n > 1:
        mid = n// 2
        S=L[:mid]
        D=L[mid:]
        mergeSort(S,len(S))
        mergeSort(D,len(D))
        i=j=k=0
        while i<len(S) and j<len(D):
            if S[i]<=D[j]:
                L[k]=S[i]
                i+=1
            else:
                L[k]=D[j]
                j+=1
            k+=1
        while i < len(S):
            L[k]=S[i]
            i+=1
            k+=1

        while j < len(D):
            L[k] = D[j]
            j+=1
            k+=1
def maxim(L,n):
    vmax=L[0]
    for i in range(1,n):
        if L[i]>vmax:
            vmax=L[i]
    return vmax
def RadixSortBaza16(L,n):
    A = [[0] for i in range(16)]
    lmax = maxim(L, n)
    placemant = 1
    radix = 16
    while lmax != 0:
        for i in range(n):
            temp = L[i] // placemant
            index = temp % radix
            if A[index][0] == 0:
                A[index][0] = L[i]
            else:
                A[index].append(L[i])
        k = 0
        for i in range(16):
            for j in range(len(A[i])):
                if A[i][j] != 0:
                    L[k] = A[i][j]
                    k += 1
                    A[i][j] = 0
        placemant=placemant<<4
        lmax=lmax>>4
def RadixSortBaza2la8(L,n):
    A = [[0] for i in range(pow(2,8))]
    lmax = maxim(L, n)
    placemant = 1
    radix = pow(2,8)
    while lmax != 0:
        for i in range(n):
            temp = L[i]//placemant
            index = temp % radix
            if A[index][0] == 0:
                A[index][0] = L[i]
            else:
                A[index].append(L[i])
        k = 0
        for i in range(pow(2,8)):
            for j in range(len(A[i])):
                if A[i][j] != 0:
                    L[k] = A[i][j]
                    k += 1
                    A[i][j]=0
        placemant=placemant<<8
        lmax=lmax>>8
def RadixSortBaza2la16(L,n):
    A = [[0] for i in range(pow(2,16))]
    lmax = maxim(L, n)
    placemant = 1
    radix =pow(2,16)
    while lmax != 0:
        for i in range(n):
            temp = L[i] // placemant
            index = temp % radix
            if A[index][0] == 0:
                A[index][0] = L[i]
            else:
                A[index].append(L[i])
        k = 0
        for i in range(pow(2,16)):
            for j in range(len(A[i])):
                if A[i][j] != 0:
                    L[k] = A[i][j]
                    k += 1
                    A[i][j] = 0
        placemant=placemant<<16
        lmax=lmax>>16

def shellSort(L,n):
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            k=L[i]
            j=i
            while j>=gap and L[j-gap]>k:
                L[j]=L[j-gap]
                j-=gap
            L[j]=k
        gap=gap//2
def SortarePython(L,n):
    L.sort()
def test_sort(L):
    ok=0
    for i in range(1,len(L)):
        if L[i]<L[i-1]:
            ok=1
    if ok==0:
        return "corect"
    return "gresit"
sorts=[SortarePython,shellSort,RadixSortBaza2la16,RadixSortBaza16,RadixSortBaza2la8,mergeSort,InsertionSort,CountingSort]
f=open("teste.txt")
g=open("output.txt","w")
s=f.readline()
nrteste=int(s[2:])
s=f.readline()
tests=[]
for i in range(nrteste):
    s=s.split()
    tests.append([int(s[0][2:]),int(s[1][4:])])
    s=f.readline()
k=1
for test in tests:
    g.write(f"Sortarile pentru testul {k}:\n")
    L=[]
    for i in range(test[0]):
        L.append(random.randint(0,test[1]))
    R=L
    for sort in sorts:
        #g.write(f"Testul={k} N={test[0]} Max={test[1]}\n")
        time_start=perf_counter()
        sort(L,test[0])
        time_stop=perf_counter()
        g.write(f"{sort}:{time_stop-time_start} a sortat {test_sort(L)}\n")
        L=R
    k+=1
f.close()
g.close()
