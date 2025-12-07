def extract_ivs(packets):
  ivs = []

    for p in packets:
        # just appends a placeholder if the packet has a 'wepdata' field fpr now
        if hasattr(p, "wepdata"):
            ivs.append("dummy-iv")

    print(f"[iv_extraction] Extracted {len(ivs)} IVs (stub)")
    return ivs
  
