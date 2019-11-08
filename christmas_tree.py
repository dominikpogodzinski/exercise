from time import time


def christmas_tree_generator(branches_amount):
    return "\n".join([" " * (branches_amount - i) + "*" * (i * 2 - 1) for i in range(1, branches_amount + 1)])


if __name__ == '__main__':
    t_start = time()
    print(christmas_tree_generator(6))
    t_end = time()

    print(f'Time of execution: {t_end - t_start}')
