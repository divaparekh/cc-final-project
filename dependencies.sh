#!/bin/sh
git clone https://github.com/divaparekh/cc-final-project.git
git clone git://github.com/mininet/mininet
mininet/util/install.sh -a
sudo apt install python3-pip
sudo apt install python-numpy
sudo apt install python-pandas
sudo apt install python-matplotlib
cd cc-final-project
pip3 install jupyter
~/.local/bin/jupyter-notebook password
