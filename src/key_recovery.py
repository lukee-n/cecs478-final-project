def run_recovery(ivs):
    print(f"[key_recovery] Received {len(ivs)} IVs")

    # TODO: integrate aircrack-ng / real WEP attack.
    key = None
    info = {
        "method": "stub",
        "note": "real key recovery not implemented yet",
    }
    return key, info
