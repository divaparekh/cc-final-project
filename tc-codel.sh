sudo tc qdisc replace dev eth0 root codel
sudo tc qdisc replace dev lo root codel
sudo tc qdisc replace dev s1-eth1 root codel
sudo tc qdisc replace dev s2-eth1 root codel
sudo tc qdisc replace dev s1-eth2 root codel
sudo tc qdisc replace dev s2-eth2 root codel
sudo tc qdisc show
