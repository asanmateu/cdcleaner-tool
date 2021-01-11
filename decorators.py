from functools import wraps
import time


def timer(func):
    """A decorator that prints how long a function took to run.

    Args:
        func (callable): The function being decorated

    Returns:
        callable: The decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_total = time.time() - t_start
        print("{} took {}s".format(func.__name__, t_total))

        return result

    return wrapper


def print_return_type(func):
    """A decorator that prints the input function's return type when debugging.

    Args:
        func (callable): The function being decorated

    Returns:
        callable: The decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(func.__name__, type(result)))

        return result

    # Return the decorated function
    return wrapper


def counter(func):
    """Adds a counter of how many times the functions being decorated are used.

    Args:
        func (callable): The function being decorated

    Returns:
        callable: The decorated function
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper
