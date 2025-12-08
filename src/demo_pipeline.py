import sys
import os
# import json
import time

from src.parser import parse_pcap
from src.iv_extraction import extract_ivs
from src.key_recovery import recover_key_from_pcap
from src.metrics import save_metrics


def main():
    """
    End-to-end demo pipeline:

    PCAP -> parse -> IV extraction -> key recovery -> metrics.json
    """
    # Allow optional CLI argument for the PCAP path
    if len(sys.argv) > 1:
        pcap_path = sys.argv[1]
    else:
        pcap_path = "data/sample.pcap"

    if not os.path.exists(pcap_path):
        raise FileNotFoundError(f"PCAP file not found: {pcap_path}")

    print(f"[demo] Starting WEP forensics pipeline on: {pcap_path}")
    start = time.time()

    # 1. Parse PCAP
    print("[demo] Parsing PCAP...")
    packets = parse_pcap(pcap_path)

    # 2. Extract IVs
    print("[demo] Extracting WEP IVs...")
    ivs = extract_ivs(packets)
    
    # 3. Run key recovery (aircrack-ng wrapper)
    print("[demo] Running key recovery via aircrack-ng...")
    key, recovery_info = recover_key_from_pcap(pcap_path)

    elapsed = time.time() - start
    print(f"[demo] Pipeline finished in {elapsed:.2f} seconds")

    # 4. Assemble metrics
    metrics = {
        "pcap": pcap_path,
        "packet_count": len(packets),
        "iv_count": len(ivs),
        "key_recovered": key is not None,
        "recovered_key": key,
        "elapsed_seconds": elapsed,
    }

    metrics.update(recovery_info)  # include info from aircrack-ng run (command, exit_code, etc.)

    # 5. Save metrics to artifacts/release/metrics/metrics.json
    save_metrics(metrics)


if __name__ == "__main__":
    main()
