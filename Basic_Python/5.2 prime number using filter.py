def is_prime(n):
    if n <=1:
        return False
    for i in range(2, int(n**.5)+1):
        if n%2 ==0:
            return False
    return True    
if __name__ == "__main__":
    numbers = range(1,101)
    primeNumbers = list(filter(is_prime, numbers))
    print(primeNumbers)