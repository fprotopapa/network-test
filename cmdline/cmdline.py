import argparse
import random
import ipaddress

class Cmd:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--dip", help="Receiver's IP",
                    type=str)
        self.parser.add_argument("--dmac", help="Receiver's MAC",
                    type=str)
        self.parser.add_argument("--dif", help="Receiver's interface",
                    type=str)
        self.parser.add_argument("--sip", help="Sender's IP",
                    type=str)
        self.parser.add_argument("--smac", help="Sender's MAC",
                    type=str)
        self.parser.add_argument("--sif", help="Sender's interface",
                    type=str)
        self.parser.add_argument('--fwd', default=False, action=argparse.BooleanOptionalAction)
        self.args = self.parser.parse_args()
    
    def is_fwd(self):
        return self.args.fwd

    def get_dst_if(self):
        return self.args.dif
    
    def get_src_if(self):
        return self.args.sif
    
    def get_dst_ip(self):
        if self.args.dip is not None:
            return self.args.dip
        else:
            return self.get_rnd_ip4()

    def get_src_ip(self):
        if self.args.sip is not None:
            return self.args.sip
        else:
            return self.get_rnd_ip4()

    def get_dst_mac(self):
        if self.args.dip is not None:
            return self.args.dip
        else:
            return self.get_rnd_mac()

    def get_src_mac(self):
        if self.args.sip is not None:
            return self.args.sip
        else:
            return self.get_rnd_mac()
        
    def get_rnd_ip4(self):
        return str(ipaddress.IPv4Address(random.randint(0,2 ** 32)))
    
    def get_rnd_mac(self):
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))