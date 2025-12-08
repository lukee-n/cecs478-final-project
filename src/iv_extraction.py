from typing import List
from scapy.layers.dot11 import Dot11WEP

def extract_ivs(packets) -> List[str]:
  """
  Extract WEP IVs from 802.11 WEP-encrypted packets
  Returns a list of IVs as hex strings, ex: "aa:bb:cc"
  """
  ivs: List[str] = []

    for p in packets:
        if p.haslayer(Dot11WEP):
            wep_layer = p[Dot11WEP]
            iv_bytes = bytes(wep_layer.iv)  # 3 bytes

            if len(iv_bytes) == 3:
                iv_str = ":".join(f"{b:02x}" for b in iv_bytes)
                ivs.append(iv_str)

    print(f"[iv_extraction] Extracted {len(ivs)} WEP IVs")
    return ivs
  
