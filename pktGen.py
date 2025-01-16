import scapy.all as scapy
import inspect

class PktGen:
    def __init__(self, interfaces = None, ):
        self.ifs = []
        self.IPList = []
        self.ARPList = []
        if isinstance(interfaces, list):
            self.ifs.append(interfaces)
        else:
            self.ifs = interfaces

    def test_icmp(self, ip):
        print('>>>>> ' + PktGen.test_icmp.__qualname__ + ' <<<<<')
        pkt = scapy.IP(dst=ip)/scapy.ICMP()
        self.IPList.append(pkt)
        pkt.show()
        ans = scapy.sr1(pkt)
        if ans is not None:
            ans.show()
            self.IPList.append(ans)

    def test_arp(self, ip):
        print('>>>>> ' + PktGen.test_arp.__qualname__ + ' <<<<<')
        pkt = pkt=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")/scapy.ARP(pdst=ip)
        self.ARPList.append(pkt)
        pkt.show()
        ans = scapy.sr1(pkt, timeout=2)
        if ans is not None:
            ans.show()
            self.ARPList.append(ans)

    def show_wireshark(self):
        scapy.wireshark(self.ARPList)
        scapy.wireshark(self.IPList)
