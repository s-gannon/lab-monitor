#!/bin/sh

DIR_PATH='/home/lab-monitor/lab-monitor'
HOSTS='katherine2 rockhopper'

if [ $HOSTS = '' ]
then
	for host in $@
	do
		scp -q lab-monitor@$host:$DIR_PATH/data/data.csv $DIR_PATH/data/data1.csv
	done
else
	for host in $HOSTS
	do
		scp -q lab-monitor@$host:$DIR_PATH/data/data.csv $DIR_PATH/data/data1.csv
	done
fi
