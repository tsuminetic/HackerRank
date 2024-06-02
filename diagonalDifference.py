#code 4 years ago (lol)

def diagonal_Difference(arr,n):
    first_no=0
    count=0
    for i in range(n):
        first_no+=arr[count][count]
        count+=1


    second_no=0
    count1=0
    count_=n
    for i in range(n):
        second_no+=arr[count1][count_-1]
        count_-=1
        count1+=1


    ans=list(str(first_no-second_no))
    
    if int("".join(ans)) < 0: 
        ans.remove('-')
        
    return int("".join(ans))


def diagonalDifference(arr):
    diagonal1=0
    diagonal2=0
    for i in range(len(arr)):
        diagonal1+=arr[i][i]
        diagonal2+=arr[i][len(arr)-1-i]
    return abs(diagonal1-diagonal2)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))