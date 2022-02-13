#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT
function ctrl_c() {
        echo "Exiting..."
        kill $P1
}

echo THIS WILL NOT WORK WITH RECENT CHANGES BUT IT WILL PROBABLY BE REPLACES ANYWAY

cd /home/ethan/Sync/Code\ Workspace/PYTHON3/Discord\ Bottobulous/

mkdir build
cd build

rm -r ./deploy/
mkdir deploy
cd deploy

# start the http server in the background and store the pid number in P1 to kill later
python3 ../../basic_http_server.py &
P1=$!

tar -czf Discord-Bot.tar.gz ../../../Discord\ Bottobulous/


# now to make it actually connect to the discord bot and deploy the bot (somehow :3)

wait
