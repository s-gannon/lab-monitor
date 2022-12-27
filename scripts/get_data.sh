#!/bin/sh

DIR_PATH='/home/lab-monitor/lab-monitor'

sshfs lab-monitor@euler.valpo.edu:$DIR_PATH/data/data.csv /home/lab-monitor/data/data1.csv
sshfs lab-monitor@germain.valpo.edu:$DIR_PATH/data/data.csv /home/lab-monitor/data/data2.csv
sshfs lab-monitor@katherine2.valpo.edu:$DIR_PATH/data/data.csv /home/lab-monitor/data/data3.csv
sshfs lab-monitor@rockhopper.valpo.edu:$DIR_PATH/data/data.csv /home/lab-monitor/data/data4.csv

