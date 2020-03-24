from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os

log = core.getLogger()

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        stop = of.ofp_match()
        #stop.in_port = 'eth2'

        stop.dl_src = EthAddr("00:00:00:00:00:01")
        stop.dl_dst = EthAddr("00:00:00:00:00:02")

        flow = of.ofp_flow_mod()
        flow.match = stop
        event.connection.send(flow)
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    print("HI FIREWALL")
    core.registerNew(Firewall)