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
    bw_high = float(sys.argv[1])
    bw_low = float(sys.argv[2])
    qdisc = sys.argv[3]
    transport = sys.argv[4]
    num_of_trials = int(sys.argv[5])
    
    def build(self, num_trials=num_of_trials, bw_hi=bw_high, bw_lo=bw_low, qdisc=qdisc,\
        transport=transport):

        source_file = open('run_trials.sh',"w+")

        for trial in range(1, num_trials + 1):
    
            host1_str = "h" + str(trial * 2 - 1)
            host2_str = "h" + str(trial * 2)

            host1_ip = '10.0.0.' + str(trial * 2 - 1)
            host2_ip = '10.0.0.' + str(trial * 2)

            host1 = self.addHost(host1_str, ip=host1_ip)
            host2 = self.addHost(host2_str, ip=host2_ip)

            s1 = self.addSwitch('s1')
            s2 = self.addSwitch('s2')

            self.addLink(host1_str, s1, bw=bw_hi, max_queue_size=100)
            self.addLink(s1, s2, bw=bw_lo)
            self.addLink(s2, host2_str, bw=bw_hi)
            
            # write to source file
            server_cmd = "py net.get('" + host2_str + "').cmd('./D-ITG-2.8.1-r1023/bin/ITGRecv &')\n"
            client_cmd = "py net.get('" + host1_str + "').cmd('./D-ITG-2.8.1-r1023/bin/ITGSend cc-final-project/shell_scripts/multiflow-tcp.sh -l ./cc-final-project/server_outputs/TO_DELETE.log -x ./cc-final-project/server_outputs/" + qdisc + "-" + transport + "-" + str(bw_hi) + "-" + str(trial) + ".log')\n"
            
            source_file.write(server_cmd)
            source_file.write(client_cmd)

        source_file.close()

def run_network():
    topo = Basic_Topo()
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

