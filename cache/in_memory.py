from functools import lru_cache


@lru_cache(maxsize=128)
def cached_fib(n: int) -> int:
    if n <= 1:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)


@lru_cache(maxsize=128)
def cached_fact(n: int) -> int:
    return 1 if n <= 1 else n * cached_fact(n - 1)


@lru_cache(maxsize=128)
def cached_pow(x: int, y: int) -> int:
    return x**y
