sudo tc qdisc replace dev eth0 root htb
sudo tc qdisc replace dev lo root htb
sudo tc qdisc replace dev s1-eth1 root htb
sudo tc qdisc replace dev s2-eth1 root htb
sudo tc qdisc replace dev s1-eth2 root htb
sudo tc qdisc replace dev s2-eth2 root htb
sudo tc qdisc show
