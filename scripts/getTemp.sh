cat /sys/bus/w1/devices/28-0214813de5ff/w1_slave |grep "t="|awk -F "t=" '{print $2/1000}'

