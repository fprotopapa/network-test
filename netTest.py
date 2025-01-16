import pyshark
# import scapy.all as scapy
import pktGen as generator

def capture_live_packets(network_interface):
    capture = pyshark.LiveCapture(interface=network_interface)
    for raw_packet in capture.sniff_continuously():
        print(filter_all_tcp_traffic_file(raw_packet))

def get_packet_details(packet):
    """
    This function is designed to parse specific details from an individual packet.
    :param packet: raw packet from either a pcap file or via live capture using TShark
    :return: specific packet details
    """
    protocol = packet.transport_layer
    source_address = packet.ip.src
    source_port = packet[packet.transport_layer].srcport
    destination_address = packet.ip.dst
    destination_port = packet[packet.transport_layer].dstport
    packet_time = packet.sniff_time
    return f'Packet Timestamp: {packet_time}' \
           f'\nProtocol type: {protocol}' \
           f'\nSource address: {source_address}' \
           f'\nSource port: {source_port}' \
           f'\nDestination address: {destination_address}' \
           f'\nDestination port: {destination_port}\n'


def filter_all_tcp_traffic_file(packet):
    """
    This function is designed to parse all the Transmission Control Protocol(TCP) packets
    :param packet: raw packet
    :return: specific packet details
    """
    if hasattr(packet, 'tcp'):
       results = get_packet_details(packet)
       return results

# capture_live_packets('enp0s25')
# def send_icmp(ip)
#     scapy.sr(scapy.IP(dst="192.168.0.1")/scapy.ICMP())

if __name__ == '__main__':
    gen = generator.PktGen('enp0s25')
    gen.test_icmp('192.168.0.1')
    gen.test_arp('192.168.0.1')
    gen.show_wireshark()