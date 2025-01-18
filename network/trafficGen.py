import scapy.all as scapy
from .interface import Interface

class TrafficGen:
    def __init__(self, timeout=None):
        self.timeout = timeout

    def send_pkt(self, pkt: scapy.Packet, port: Interface, timeout = None):
        pktList = []
        if timeout is None:
            timeout = self.timeout
        pktList.append(pkt)
        ans, _ = scapy.srp(pkt, timeout=self.timeout, iface=port.intf)
        for _,rcv in ans:
            pktList.extend([rcv])
        return scapy.PacketList(pktList)