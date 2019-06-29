#!/usr/bin/env python2
from collections import deque

import tasks

results = deque([])

for i in range(1, 42):
    if i % 15 == 0:
        results.append(tasks.hello.delay('{} FizzBuzz'.format(i)))
    elif i % 3 == 0:
        results.append(tasks.hello.delay('{} Fizz'.format(i)))
    elif i % 5 == 0:
        results.append(tasks.hello.delay('{} Buzz'.format(i)))
    else:
        results.append(tasks.hello.delay('{}'.format(i)))

print('All queue were enqueued')

#while len(results) > 0:
#    result = results.popleft()
#    if result.ready():
#        print(result.get())
#        continue
#
#    results.append(result)
