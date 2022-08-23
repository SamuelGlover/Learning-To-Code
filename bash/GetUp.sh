#!/bin/bash

name=$1
drink=$2


user=$(whoami)
date=$(date)
whereami=$(pwd)

echo "Good Morning $name. You've got a lot to learn today."
sleep 1
echo "You're lookin pretty damn sleepy today. Go get some $drink."
sleep 1
echo "Nice, looks like you're ready for this session. Break is over. lets get at it"
sleep 2
echo "At the time of correspondence you are logged in as $user, and you are in the directory $whereami, and it is $date"
