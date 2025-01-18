import re
import sys
from ipaddress import IPv6Address, ip_address

class Interface:
    portCnt = 0
    def __init__(self, ifName, ip, mac):
        self.intf = ifName
        self.ip = self._val_ip(ip)
        self.mac = self._val_mac(mac)
        type(self).portCnt += 1
        self.port = type(self).portCnt

    def _val_ip(self, ip):
        try:
            ip_obj = ip_address(ip)
        except ValueError:
            print(f"ERROR: {ip} is not a valid IP address!")
            sys.exit(-1)
        if isinstance(ip_obj, IPv6Address):
            self.ipv6 = True
        else:
            self.ipv6 = False
        return ip_obj
    
    def _val_mac(self, mac):
        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
            return mac
        else:
            print(f"ERROR: {mac} is not a valid MAC address!")
            sys.exit(-1)