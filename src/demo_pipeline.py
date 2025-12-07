from parser import parse_pcap
from iv_extraction import extract_ivs
from key_recovery import recover_key
from metrics import save_metrics

def main():
    pcap_path = "data/sample_wep.pcap"
    packets = parse_pcap(pcap_path)
    ivs = extract_ivs(packets)
    key, stats = recover_key(ivs)
    save_metrics(key, stats)

if __name__ == "__main__":
    main()
