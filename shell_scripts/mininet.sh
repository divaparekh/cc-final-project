#!/bin/bash
sudo mn -c
sudo python mininet/custom/basic.py $1 1
sudo mn -c
sudo python mininet/custom/basic.py $1 2.5
sudo mn -c
sudo python mininet/custom/basic.py $1 5
sudo mn -c
sudo python mininet/custom/basic.py $1 10
sudo mn -c
sudo python cc-final-project/convert_ditg_logs.py
#sudo rm ~/cc-final-project/server_outputs/*.log
