def memoize(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]

    return inner


@memoize
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

num=int(input("Enter the number to find it's factorial"))
print("the factorial of given number is ",factorial(num))

