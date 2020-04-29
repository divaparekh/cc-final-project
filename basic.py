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
    def build(self, bw_high=5):
        info('*** Adding hosts\n')
        h1 = self.addHost('h1', ip='10.0.0.1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', ip='10.0.0.2', mac='00:00:00:00:00:02')
        
        #h3 = self.addHost('h3', ip='10.0.0.3', mac='00:00:00:00:00:03')

        info('*** Adding switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        info('*** Adding links\n')
        bw_low = float(bw_high/10.0)
        self.addLink(h1, s1, bw=bw_high, max_queue_size=100)
        self.addLink(s1, s2, bw=bw_low)
        self.addLink(s2, h2, bw=bw_high)

        #bw_high = float(sys.argv[1])
        #bw_low = float(sys.argv[2])
        #transport = sys.argv[3]
        num_trials = int(sys.argv[1])

        source_file = open('run_trials.sh',"w+")

        server_cmd = "py net.get('h2').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')\n"
        source_file.write(server_cmd)

        for qdisc in ['pie']: #['noqueue','codel','fq_codel', 'pie]:

            source_file.write("py net.get('s1').cmdPrint('sudo tc qdisc replace dev s1-eth1 root " + qdisc + "')\n")
            source_file.write("py net.get('s2').cmdPrint('sudo tc qdisc replace dev s2-eth1 root " + qdisc + "')\n")
            source_file.write("py net.get('s2').cmdPrint('sudo tc qdisc replace dev s2-eth2 root " + qdisc + "')\n")
            source_file.write("py net.get('s1').cmdPrint('sudo tc qdisc replace dev s1-eth2 root tbf rate " + str(bw_low) + "mbit burst 32kbit latency 22000000000ms')\n")
            
            for transport in ['tcp', 'udp']:
                '''
                for bw_high in [1.0, 2.5, 5.0, 10.0]:
                    bw_low = float(bw_high/10.0)
                '''


                for trial in range(1, num_trials + 1):
                    client_cmd = "py net.get('h1').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-" + transport + ".sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/" + qdisc + "-" + transport + "-" + str(bw_high) + "-" + str(trial) + ".log')\n"
                    source_file.write(client_cmd)

        #source_file.write('exit\n')
        source_file.close()


def run_network():

    #for bw_high in [1.0, 2.5, 5.0, 10.0]:

    bw_high = float(sys.argv[2])
    topo = Basic_Topo(bw_high=bw_high)
    net = Mininet(topo, link=TCLink)
    net.start()
    info('*** Starting network\n')
    print("Dumping host connections")
    dumpNodeConnections(net.hosts)
    
    info('*** Running CLI')
    CLI(net)

    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run_network()
