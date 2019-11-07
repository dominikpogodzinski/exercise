from functools import lru_cache
from my_decorator import check_if_logged_in


@lru_cache(maxsize=1000)
@check_if_logged_in
def fibonacci(n):
    if n in (1, 2):
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(1, 11):
    print("{}: {}".format(i, fibonacci(i)), 'python')
