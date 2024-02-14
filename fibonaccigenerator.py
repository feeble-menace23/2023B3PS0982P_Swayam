num = int(input("enter the number of elements for the fibonacci sequence\n"));
def fibonacci(n):
    if n in {0, 1}:
        return n;
    return fibonacci(n-1) + fibonacci(n-2);

print([fibonacci(i) for i in range(num)]);
