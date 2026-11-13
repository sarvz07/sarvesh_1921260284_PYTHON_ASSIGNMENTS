import cProfile
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(message)s')

def sample(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

print('assert check:', sample(10))
assert sample(10) == 285
logging.info('Logging is useful for runtime diagnostics.')
start = time.perf_counter(); sample(50000); print('Timing:', time.perf_counter()-start)
prof = cProfile.Profile(); prof.enable(); sample(50000); prof.disable(); prof.print_stats(sort='time')
print('This demonstrates why logging and cProfile are more effective than print-only debugging.')
