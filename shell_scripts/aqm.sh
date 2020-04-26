#!/bin/bash

if [ "$1" == "codel" ]
then
	sudo tc qdisc replace dev eth0 root codel
	sudo tc qdisc replace dev lo root codel
	sudo tc qdisc replace dev s1-eth1 root codel
	sudo tc qdisc replace dev s2-eth1 root codel
	sudo tc qdisc replace dev s2-eth2 root codel

elif [ "$1" == "noqueue" ]
then
	sudo tc qdisc replace dev eth0 root noqueue
	sudo tc qdisc replace dev lo root noqueue
	sudo tc qdisc replace dev s1-eth1 root noqueue
	sudo tc qdisc replace dev s2-eth1 root noqueue
	sudo tc qdisc replace dev s2-eth2 root noqueue

elif [ "$1" == "red" ]
then
	sudo tc qdisc replace dev eth0 root red
	sudo tc qdisc replace dev lo root red
	sudo tc qdisc replace dev s1-eth1 root red
	sudo tc qdisc replace dev s2-eth1 root red
	sudo tc qdisc replace dev s2-eth2 root red

elif [ "$1" == "pie" ]
then
	sudo tc qdisc replace dev eth0 root pie
	sudo tc qdisc replace dev lo root pie
	sudo tc qdisc replace dev s1-eth1 root pie
	sudo tc qdisc replace dev s2-eth1 root pie
	sudo tc qdisc replace dev s2-eth2 root pie

else
	echo "Enter a parameter for the type of queuing mechanism you would like to implement. Options are noqueue, red, codel, and pie."

fi

sudo tc qdisc replace dev s1-eth2 root tbf rate .5mbit burst 32kbit latency 22000000000ms
sudo tc qdisc show
