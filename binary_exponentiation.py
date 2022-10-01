def binary_exponentiation(a,b):
    ans=1
    while(b):
        if(b&1):
            ans=ans*a
        a=a*a
        b=b>>1
    return ans
if __name__=='__main__':
    n=list(map(int,input().strip().split()))
    a=n[0]
    b=n[1]
    result = binary_exponentiation(a,b)
    print(result)