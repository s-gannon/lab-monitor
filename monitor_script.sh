#!/bin/sh
top -o -%CPU -b -n 1 | tail -3 > processes.txt
#	5 numbers from the CPU column
top -o -%CPU -b -n 1 | tail -5 | awk '{print $9}' > total_cpu.txt
#	$2 -> TOTAL RAM $3 -> USED RAM
#free -g | grep Mem | awk '{print $2","$3}' > total_gpu.txt

#	$9 -> CPU USAGE $10 -> GPU USAGE $12 -> TASK NAME
hostname > data.csv	#hostname
ifconfig | grep 'inet 192' | awk '{print $2}' >> data.csv	#address
#alive
paste -s -d+ total_cpu.txt | bc >> data.csv
free -g | grep Mem | awk '{print $2}' >> data.csv	#max RAM
free -g | grep Mem | awk '{print $3}' >> data.csv	#used RAM
awk '{print $9","$10","$12}' processes.txt >> data.csv	#tasks
