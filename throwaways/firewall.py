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
        stopTop = of.ofp_match()
        stopBottom = of.ofp_match()

        stopBottom.dl_src = EthAddr("00:00:00:00:00:01")
        stopBottom.dl_dst = EthAddr("00:00:00:00:00:14")

	stopTop.dl_src = EthAddr("00:00:00:00:00:02")
	stopTop.dl_dst = EthAddr("00:00:00:00:00:12")

		
	#mod_dl_src:mac
	#mod_dl_dst:mac

	#stop.dl_src = "00:00:00:00:00:01"
	#stop.dl_dst = "00:00:00:00:00:02"

        flowTop = of.ofp_flow_mod()
        flowTop.match = stopTop

	flowBottom = of.ofp_flow_mod()
	flowBottom.match = stopBottom

        event.connection.send(flowTop)
	event.connection.send(flowBottom)
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    print("HI FIREWALL")
    core.registerNew(Firewall)
