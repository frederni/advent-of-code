import time
def test_performance(func1, func2, n_runs, *args):
    print(f"Running functions {n_runs} times ...")
    t0 = time.time()
    for _ in range(n_runs):
        func1(*args)
    duration_func1 = time.time() - t0

    t0 = time.time()
    for _ in range(n_runs):
        func2(*args)
    duration_func2 = time.time() - t0
    print(f"First function: {duration_func1} s, second function: {duration_func2} s")
    return duration_func1, duration_func2
