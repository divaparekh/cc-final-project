sudo tc qdisc replace dev eth0 root red limit 1000 avpkt 1000
sudo tc qdisc replace dev lo root red limit 1000 avpkt 1000
sudo tc qdisc replace dev s1-eth1 root red limit 1000 avpkt 1000
sudo tc qdisc replace dev s2-eth1 root red limit 1000 avpkt 1000
sudo tc qdisc replace dev s1-eth2 root red limit 1000 avpkt 1000
sudo tc qdisc replace dev s2-eth2 root red limit 1000 avpkt 1000
sudo tc qdisc show
