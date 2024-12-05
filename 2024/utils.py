import time
from typing import Callable

def test_performance(func1: Callable, func2: Callable, *args, **kwargs):
    verbose = kwargs.get("verbose", False)
    n_runs = kwargs.get("n_runs", 1)
    if verbose:
        print(f"Running functions {n_runs} times ...")
    t0 = time.time()
    for _ in range(n_runs):
        func1(*args)
    duration_func1 = time.time() - t0

    t0 = time.time()
    for _ in range(n_runs):
        func2(*args)
    duration_func2 = time.time() - t0
    if verbose:
        print(f"First function: {duration_func1} s, second function: {duration_func2} s")
    return duration_func1, duration_func2

def parse_raw(file_path: str):
    with open(file_path, 'r') as f:
        data =  f.read()
    return data