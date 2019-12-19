def Fibonacci(FibonacciIndex):

    if FibonacciIndex == 0:
        print("Fibonacci index in incorrect")
    elif FibonacciIndex == 1:
        return 0
    elif FibonacciIndex == 2:
        return 1
    else:
        return Fibonacci(FibonacciIndex - 1) + Fibonacci(FibonacciIndex - 2)