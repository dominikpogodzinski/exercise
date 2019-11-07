def sprawdz_czy_zalogowany(funkcja_dekorowana):
    def new_func(*args, **kwargs):
        print("hello :P")
        return funkcja_dekorowana(*args, **kwargs)

    return new_func
