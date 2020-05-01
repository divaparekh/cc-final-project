#!/bin/sh
cd ~/.
git clone git://github.com/mininet/mininet
mininet/util/install.sh -a
cp ./cc-final-project/basic.py ./mininet/custom/
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 install jupyter
wget http://www.grid.unina.it/software/ITG/codice/D-ITG-2.8.1-r1023-src.zip
unzip D-ITG-2.8.1-r1023-src.zip
cd D-ITG-2.8.1-r1023/src
make
cd ~/.
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
sudo rm ~/cc-final-project/server_outputs/*.log
~/.local/bin/jupyter-notebook password
~/.local/bin/jupyter-notebook cc-final-project/run-group9.ipynb --ip=0.0.0.0
