import asyncio


async def fibonacci(n):
    if n <= 1:
        return n
    else:
        return await asyncio.gather(fibonacci(n-1), fibonacci(n-2))


async def factorial(n):
    if n == 0:
        return 1
    else:
        return n * await factorial(n-1)


async def squares(n):
    return [i**2 for i in range(n)]


async def cubic(n):
    return [i**3 for i in range(n)]


async def main():
    numbers = list(range(1, 11))

    fib_results = await asyncio.gather(*(fibonacci(num) for num in numbers))
    fact_results = await asyncio.gather(*(factorial(num) for num in numbers))
    squares_results = await asyncio.gather(*(squares(num) for num in numbers))
    cubic_results = await asyncio.gather(*(cubic(num) for num in numbers))

    print("Fibonacci Results:", fib_results)
    print("Factorial Results:", fact_results)
    print("Squares Results:", squares_results)
    print("Cubic Results:", cubic_results)

if __name__ == "__main__":
    asyncio.run(main())
    
