#!/bin/sh
git clone git://github.com/mininet/mininet
mininet/util/install.sh -a
cp ./cc-final-project/basic.py ./mininet/custom/
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
cd cc-final-project
pip3 install jupyter

# Mininet run lines go here
cd ..
sudo mn -c
sudo python mininet/custom/basic.py 5 .5

cd cc-final-project
~/.local/bin/jupyter-notebook password
~/.local/bin/jupyter-notebook run-group9.ipynb --ip=0.0.0.0
