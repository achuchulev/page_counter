#!/usr/bin/env bash

#test cli app
out=$(python app.py)
if [ "$out" > 0 ]; then
  echo Good
else
  echo Bad
  exit 1
fi


# start our webapp
python webapp.py &
# sleep so web app is up and running
sleep 3

# test webapp
out2=$(curl -sL http://127.0.0.1:8080)
if [ "$out2" > 0 ]; then
  echo Good
else
  echo Bad
  exit 1
fi

