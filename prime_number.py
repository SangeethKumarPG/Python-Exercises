def prime_checker(number):
    isPrime = True
    for i in range(2,int(number/2)):
        if number % i == 0:
            isPrime = False
    if isPrime == True:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")



n = int(input("Enter the number : "))
prime_checker(number=n)