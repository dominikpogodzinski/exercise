def check_if_logged_in(func_decorator):
    def new_func(*args, **kwargs):
        print("hello :P")
        return func_decorator(*args, **kwargs)

    return new_func
