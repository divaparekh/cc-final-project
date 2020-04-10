#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
class BasicTCPTopo(Topo):
    "Two hosts with bidirectional links."
    def build(self):
        sender = self.addHost('h1')
        receiver = self.addHost('h2')
        
        link = self.addLink(sender, receiver) 
        
def simpleTest():
    "Create and test a simple network"
    topo = BasicTCPTopo()
    net = Mininet(topo)
    net.start()
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    print("Testing network connectivity")
    #net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
