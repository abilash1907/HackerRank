def countSwaps(a):
    # Write your code here
    n=len(a)
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                c+=1
    print("Array is sorted in", c ,"swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])
                
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)