#!/bin/sh

DIR_PATH='/home/lab-monitor/lab-monitor'

scp lab-monitor@euler.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data1.csv
scp lab-monitor@germain.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data2.csv
scp lab-monitor@katherine2.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data3.csv
scp lab-monitor@rockhopper.valpo.edu:$DIR_PATH/data/data.csv $DIR_PATH/data/data4.csv

