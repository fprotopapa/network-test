import scapy.all as scapy

class Visual:
    def show_packets(self, pktLst: scapy.PacketList):
        print('Packets:')
        for pkt in pktLst:
            pkt.show()
        print('')

    def dump_packets(self, pktLst: scapy.PacketList):
        print('Hexdump packets')
        for pkt in pktLst:
            pkt.summary()
            scapy.hexdump(pkt)
        print('')
    
    def print_pdf(self, pktLst: scapy.PacketList, filePath: str):
        pktLst.pdfdump( filePath, layer_shift=1)
    
    def show_summary(self, pktLst: scapy.PacketList):
        print('Packet Summary')
        pktLst.summary()
        print('')

class WireShark:
    def openWireShark(self, pktLst: scapy.PacketList):
        scapy.wireshark(pktLst)