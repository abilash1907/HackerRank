def hourglassSum(arr):
    # Write your code here
    sums=[]
    R=len(arr)
    C=len(arr[0])
    for i in range(R-2):
        for j in range(C-2):
            s=(arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            sums.append(s)
    return max(sums)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()