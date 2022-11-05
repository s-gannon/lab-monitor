#!/bin/sh
top -o -%CPU -b -n 1 | tail -3 | tac > processes.txt
#	5 numbers from the CPU column
cat processes.txt | awk '{print $9}' > total_cpu.txt
#	$2 -> TOTAL RAM $3 -> USED RAM
#free -g | grep Mem | awk '{print $2","$3}' > total_gpu.txt


hostname | awk '{print "hostname,"$1}' > data.csv	#hostname
ifconfig | grep 'inet 10' | awk '{print "address," $2}' >> data.csv	#address
awk '{print "alive,true"}' >> data.csv	#alive
paste -s -d+ total_cpu.txt | bc | awk '{print "cpu," $1}' >> data.csv
free -g | grep Mem | awk '{print "max_ram," $2}' >> data.csv	#max RAM
free -g | grep Mem | awk '{print "cur_ram," $3}' >> data.csv	#used RAM
#	$9 -> CPU USAGE $10 -> GPU USAGE $12 -> TASK NAME
awk '{i = i + 1; print "task" i "_name," $12 "\ntask" i "_cpu," $9}' processes.txt >> data.csv	#tasks

# rm *.txt
