#!/bin/sh
DATA_DIR='../data/'

top -o -%CPU -b -n 1 | tail -3 | tac > $DATA_DIR/processes.txt
#	5 numbers from the CPU column
cat processes.txt | awk '{print $9}' > $DATA_DIR/total_cpu.txt
#	$2 -> TOTAL RAM $3 -> USED RAM
#free -g | grep Mem | awk '{print $2","$3}' > total_gpu.txt


hostname | awk '{print "hostname,"$1}' > $DATA_DIR/data.csv	#hostname
ifconfig | grep 'inet 10' | awk '{print "address," $2}' >> $DATA_DIR/data.csv	#address
echo "alive,true" >> $DATA_DIR/data.csv	#alive; currently static to fix bug
paste -s -d+ total_cpu.txt | bc | awk '{print "cpu," $1}' >> $DATA_DIR/data.csv
free -g | grep Mem | awk '{print "max_ram," $2}' >> $DATA_DIR/data.csv	#max RAM
free -g | grep Mem | awk '{print "cur_ram," $3}' >> $DATA_DIR/data.csv	#used RAM
#	$9 -> CPU USAGE $10 -> GPU USAGE $12 -> TASK NAME
awk '{i = i + 1; print "task" i "_name," $12 "\ntask" i "_cpu," $9}' $DATA_DIR/processes.txt >> $DATA_DIR/data.csv	#tasks


rm $DATA_DIR/processes.txt
rm $DATA_DIR/total_cpu.txt
