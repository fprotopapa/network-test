import scapy.all as scapy
from .interface import Interface

class PktGen:
    def __init__(self):
        self.timeout = 2

    def l2(self, srcIf: Interface, dstIf: Interface):
        return scapy.Ether(dst=dstIf.mac, src=srcIf.mac)
    
    def l3(self, srcIf: Interface, dstIf: Interface):
        return scapy.Ether(dst=dstIf.mac, src=srcIf.mac)/scapy.IP(dst=str(dstIf.ip), src=str(srcIf.ip))
    
    def icmp(self, l3: scapy.Packet):
        return l3/scapy.ICMP()

    def arp(self, srcIf: Interface, dstIf: Interface):
        return scapy.Ether(dst='ff:ff:ff:ff:ff:ff', src=srcIf.mac)/scapy.ARP(pdst=str(dstIf.ip), psrc=str(srcIf.ip))
    
    def tcp(self, l3: scapy.Packet, dport: int):
        return l3/scapy.TCP(dport=dport)

    def udp(self, l3: scapy.Packet, dport: int):
        return l3/scapy.UDP(dport=dport)

    def payload(self, pkt: scapy.Packet, payload: str):
        return pkt/payload

    def packetList(pkts: list[scapy.Packet]):
        return scapy.PacketList(pkts)
