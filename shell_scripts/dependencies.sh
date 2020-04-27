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
