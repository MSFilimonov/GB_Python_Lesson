from itertools import count, cycle

stop_cycle = 10
my_list = [i for i in range(8)]
counter = count()
cycle = cycle(my_list)
print([next(counter) for i in range(a)])
print([next(cycle) for i in range(a)])
