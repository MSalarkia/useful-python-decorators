import time

class Profiler:
    def __init__(self, fn):
        self._fn = fn
        self._counter = 0
        self._total_time = 0


    def __call__(self, *args, **kwargs):
        t1 = time.perf_counter()
        result = self._fn(*args, **kwargs)
        t2 = time.perf_counter()

        self._total_time += t2 - t1
        self._counter += 1
        return result
    

    @property
    def counter(self):
        return self._counter

    @property
    def avg_time(self):
        return self._total_time / self.counter




if __name__ == '__main__':
    @Profiler
    def sum(a, b):
        return a + b


    print(sum(1, 3))
    print(sum(3, 3))
    print(sum(1, 323))
    print(sum(4, 34))
    print(sum(6, 45))
    print(sum.counter, sum.avg_time)