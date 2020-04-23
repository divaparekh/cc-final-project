#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink

import sys

class Basic_Topo(Topo):
    #Two hosts with two switches in between and
    #three links to create bottleneck
    def build(self):
        info('*** Adding hosts\n')
        h1 = self.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
        
        h3 = self.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')

        info('*** Adding switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        info('*** Adding links\n')
        
        bw_high = float(sys.argv[1])
        bw_low = float(sys.argv[2])

        self.addLink(h1, s1, bw=bw_high)# , max_queue_size=100)
        self.addLink(s1, s2, bw=bw_low)
        self.addLink(s2, h2, bw=bw_high)

def run_network():
    topo = Basic_Topo()
    net = Mininet(topo, link=TCLink)
    net.start()
    info('*** Starting network\n')
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    
    #info('*** Running CLI')
    CLI(net)

    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_network()

