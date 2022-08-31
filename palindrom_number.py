def check_palindrome(number):
    temp=number
    sum=0
    while number>=1:
        reminder =number%10
        sum = sum*10+reminder
        number=number//10
    if sum==temp:
        return True
    else:
        return False

if __name__ == '__main__':
    number = int(input().strip())
    ans=check_palindrome(number)
    if ans:
        print(f'{ number } is palindrome')
    else:
        print(f'{ number } is not palindrome')