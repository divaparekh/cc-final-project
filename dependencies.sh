#!/bin/sh
git clone git://github.com/mininet/mininet
mininet/util/install.sh -a
cp ./cc-final-project/basic.py ./mininet/custom/
sudo apt -y install python3-pip
sudo apt -y install python-numpy
sudo apt -y install python-pandas
sudo apt -y install python-matplotlib
cd cc-final-project
pip3 install jupyter

# Mininet run lines go here
cd ..
sudo python mininet/custom/basic.py 50 5
pingall

cd cc-final-project
~/.local/bin/jupyter-notebook run-group9.ipynb --ip=0.0.0.0
