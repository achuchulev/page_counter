#!/usr/bin/env python

# define count variable
count = 0
count += 1

# import statsd from DogStadts
from datadog import statsd

statsd.increment('app.cli')
print count
