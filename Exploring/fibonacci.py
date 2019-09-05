# fibonacci series with lru_cache


from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    # check whether the given number is a positive integer
    if type(n) != int:
        raise TypeError("Please specify a positive integer")
    if n < 1:
        raise ValueError("Please specify a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for n in range(1, 101):
        print(n, ":", fibonacci(n))

