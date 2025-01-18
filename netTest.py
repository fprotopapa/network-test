import os

from network import Interface, Fwd, TrafficGen, PktGen
from utils import Visual, WireShark
from cmdline import Cmd

def fill_interface(args: Cmd, isDst):
    if isDst:
        ip = args.get_dst_ip()
        mac = args.get_dst_mac()
        intf = args.get_dst_if()
    else:
        ip = args.get_src_ip()
        mac = args.get_src_mac()
        intf = args.get_src_if() 
    return Interface(intf, ip, mac)

if __name__ == '__main__':
    cmdline = Cmd()
    fwdConf = Fwd()
    traffic = TrafficGen(timeout=2)
    gen = PktGen()
    vis = Visual()
    ws = WireShark()

    isFwd = cmdline.is_fwd()
    src = fill_interface(cmdline, False)
    dst = fill_interface(cmdline, True)
    
    if isFwd:
        fwdConf.config_fwd(src, dst)
    

    l3 = gen.l3(src, dst)
    icmp = gen.icmp(l3)
    l4 = gen.tcp(l3, 1000)
    pkt = gen.payload(l4, 'Test payload')

    pktLst = traffic.send_pkt(pkt, src)
    vis.dump_packets(pktLst)
    vis.show_packets(pktLst)
    vis.print_pdf(pktLst, os.path.join(os.getcwd(), 'packetList' + '.pdf'))
    ws.openWireShark(pktLst)
    pkt = gen.arp(src, dst)
    pktLst = traffic.send_pkt(pkt, src)
    vis.show_summary(pktLst)