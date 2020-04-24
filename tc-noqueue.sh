sudo tc qdisc replace dev eth0 root noqueue
sudo tc qdisc replace dev lo root noqueue
sudo tc qdisc replace dev s1-eth1 root noqueue
sudo tc qdisc replace dev s2-eth1 root noqueue
sudo tc qdisc replace dev s1-eth2 root noqueue
sudo tc qdisc replace dev s2-eth2 root noqueue
sudo tc qdisc show
