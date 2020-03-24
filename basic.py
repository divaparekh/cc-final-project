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

        topLeftSwitch = self.addSwitch('s1')
        topRightSwitch = self.addSwitch('s2')
        bottomRightSwitch = self.addSwitch('s3')
        bottomLeftSwitch = self.addSwitch('s4')

        moreBWOpts = dict(bw='100k', delay='5ms', max_queue_size=20)
        lessBWOpts = dict(bw='10k', delay='5ms', max_queue_size=20)
        
        topLeftLink = self.addLink(sender, topLeftSwitch, **moreBWOpts)
        topMidLink = self.addLink(topLeftSwitch, topRightSwitch, **lessBWOpts)
        topRightLink = self.addLink(topRightSwitch, receiver, **moreBWOpts)

        bottomRightLink = self.addLink(receiver, bottomRightSwitch, **moreBWOpts)
        bottomMidLink = self.addLink(bottomRightSwitch, bottomLeftSwitch, **lessBWOpts)
        bottomLeftLink = self.addLink(bottomLeftSwitch, sender, **moreBWOpts)

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
