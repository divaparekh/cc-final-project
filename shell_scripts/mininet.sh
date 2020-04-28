#!/bin/bash
sudo mn -c
sudo python mininet/custom/basic.py 2 1.0
sudo mn -c
sudo python mininet/custom/basic.py 2 2.5
sudo mn -c
sudo python mininet/custom/basic.py 2 5.0
sudo mn -c
sudo python mininet/custom/basic.py 2 10.0
sudo mn -c
sudo python convert_ditg_logs.py
