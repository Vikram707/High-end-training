def sum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return(sum)   
if __name__ == "__main__":
    arr=list(map(int,input().split()))
    n=len(arr)
    ans=sum(arr)
    print(ans)   