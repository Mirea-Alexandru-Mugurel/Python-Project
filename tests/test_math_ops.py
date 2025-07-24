from cache.in_memory import cached_pow, cached_fib, cached_fact


def test_cached_fib():
    assert cached_fib(0) == 0
    assert cached_fib(1) == 1
    assert cached_fib(6) == 8


def test_cached_fact():
    assert cached_fact(0) == 1
    assert cached_fact(1) == 1
    assert cached_fact(4) == 24


def test_cached_pow():
    assert cached_pow(2, 3) == 8
    assert cached_pow(5, 0) == 1
    assert cached_pow(10, 2) == 100
