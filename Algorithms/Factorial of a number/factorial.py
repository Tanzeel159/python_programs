def factorial(n):
    if n==0:
        return 1
    if n==1:
        return n
    return n*factorial(n-1)

num=int(input("Enter the number to find it's factorial"))

print("the factorial of the given number is ",factorial(num))

