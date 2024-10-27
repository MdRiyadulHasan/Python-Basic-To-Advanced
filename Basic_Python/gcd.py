def find_gcd(a,b):
    if b==0:
        return a
    return find_gcd(b,a%b)

if __name__=='__main__':
    n=list(map(int,input().strip().split()))
    a=n[0]
    b=n[1]
    result = find_gcd(a,b)
    print(result)