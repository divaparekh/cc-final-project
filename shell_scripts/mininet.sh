#!/bin/bash
sudo mn -c
sudo python mininet/custom/diva-basic.py 2 1
sudo mn -c
sudo python mininet/custom/diva-basic.py 2 2.5
sudo mn -c
sudo python mininet/custom/diva-basic.py 2 5
sudo mn -c
sudo python mininet/custom/diva-basic.py 2 10
sudo mn -c
sudo python convert_ditg_logs.py
