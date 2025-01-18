from .interface import Interface

class Fwd:
    def __init__(self):
        self.srcs = []
        self.dsts = []
    
    def add_source(self, intf: Interface):
        self.srcs.append(intf)

    def add_destination(self, intf: Interface):
        self.dsts.append(intf)

    def config_fwd(self, src: Interface, dst: Interface):
        self.add_source(src)
        self.add_destination(dst)
        print("Forwarding not implemented")
