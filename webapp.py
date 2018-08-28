#!/usr/bin/env python

# Import statsd
from datadog import statsd
from flask import Flask

app = Flask(__name__)

#set variable to 0
count=0

@app.route("/")
def hello():
    #use the global variable instead of a local one
    global count
    #increment count by 1
    count+=1
    statsd.increment('app.web')
    return "{}".format(count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
