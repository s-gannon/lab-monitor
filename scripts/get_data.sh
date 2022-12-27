#!/bin/sh

DIR_PATH='/home/lab-monitor/lab-monitor'

touch $DIR_PATH/data/data1.csv
sshfs lab-monitor@euler.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data1.csv
touch $DIR_PATH/data/data2.csv
sshfs lab-monitor@germain.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data2.csv
touch $DIR_PATH/data/data3.csv
sshfs lab-monitor@katherine2.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data3.csv
touch $DIR_PATH/data/data4.csv
sshfs lab-monitor@rockhopper.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data4.csv

