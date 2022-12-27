# Lab Monitor
Monitors multiple PCs (Linux only), giving statistics such as CPU and RAM usage and the programs with the highest CPU usage. 

## Setup (PCs being monitored)
1. Clone the repository.
2. Edit your crontab to run `lab-monitor/scripts/monitor_script.sh` or use a different utility to run the script constantly.

## Setup (The monitor)
1. Clone the repository.
2. Edit the `lab-monitor/scripts/get_data.sh` script and change the hosts that the script will connect to.
3. Create and share keys between the monitoring PC and the PCs to be monitored.
4. Edit your crontab to run `lab-monitor/scripts/get_data.sh` or use a different utility to run the script constantly.
5. Run `python3 /src/main.py`.

## Known Bugs/Issues
- The formatting on the cells is a bit off.

## Future Features
- Dynamically sized windows / text
- A graphical version using OpenGL or Vulkan alongside the CLI version
