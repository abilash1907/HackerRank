def acmTeam(topic):
    # Write your code here
    n=len(topic)
    count=[]
    for i in range(n):
        for j in range(i+1,n):
            c=topic[i].count('1')+topic[j].count('1')
            same=0
            for k,v in zip(topic[i],topic[j]):
                if k==v=='1':
                    same+=1
            count.append(c-same)
    m=max(count)
    return [m,count.count(m)]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
