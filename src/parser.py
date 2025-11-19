from scapy.all import rdpcap

def parse_pcap(path):
    packets = rdpcap(path)
    print(f"Loaded {len(packets)} packets.")
    return packets

if __name__ == "__main__":
    parse_pcap("data/sample.pcap")
