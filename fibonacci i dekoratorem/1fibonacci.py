from functools import lru_cache
from moj_dekorator import sprawdz_czy_zalogowany


@lru_cache(maxsize=1000)
@sprawdz_czy_zalogowany
def fibonacci(n):
    if n in (1, 2):
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(1, 11):
    print("{}: {}".format(i, fibonacci(i)), 'python')
