#!/bin/bash
sudo mn -c
sudo python mininet/custom/basic.py 2 1
sudo mn -c
sudo python mininet/custom/basic.py 2 2.5
sudo mn -c
sudo python mininet/custom/basic.py 2 5
sudo mn -c
sudo python mininet/custom/basic.py 2 10
sudo mn -c
sudo python cc-final-project/convert_ditg_logs.py
#sudo rm ~/cc-final-project/server_outputs/*.log
