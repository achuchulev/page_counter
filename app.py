#!/usr/bin/env python

# import statsd from DogStadts
from datadog import statsd

# define count variable
count = 0
count += 1

statsd.event('cli app started', 'the cli app has been started', alert_type='info')
statsd.increment('app.cli')
print count
