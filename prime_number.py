def find_prime(start,end):
    prime_numbers=[]
    for i in range(start,end):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if (i%j==0):
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers

if __name__ == '__main__':
    start, end = list(map(int,input().strip().split()))
    prime_numbers = find_prime(start,end)
    print(f'prime numbers : {prime_numbers}')