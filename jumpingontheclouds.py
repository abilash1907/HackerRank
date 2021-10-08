def jumpingOnClouds(c):
    # Write your code here
    count=0
    n=len(c)
    i=0
    while i<n-1:
        if i+2<n and c[i+2]==0:
            count+=1
            i+=2
        elif i+1<n and c[i+1]==0:
                count+=1
                i+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
