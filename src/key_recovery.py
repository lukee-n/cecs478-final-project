import os
import re
import subprocess
from typing import Optional, Tuple, Dict

AIRCRACK_CMD = "aircrack-ng"


def recover_key_from_pcap(pcap_path: str) -> Tuple[Optional[str], Dict]:
    """
    Run aircrack-ng against the given PCAP and try to recover a WEP key.

    Returns (key_hex, info_dict)
      - key_hex: e.g. "12:34:56:78:90" or None if not found
      - info_dict: metadata about the run (command, exit code, stdout, stderr, note)
    """
    if not os.path.exists(pcap_path):
        raise FileNotFoundError(f"PCAP not found: {pcap_path}")

    cmd = [AIRCRACK_CMD, pcap_path]
    info: Dict[str, object] = {
        "command": " ".join(cmd),
    }

    print(f"[key_recovery] Running: {' '.join(cmd)}")

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        # aircrack-ng not installed (ex:, in CI)
        print("[key_recovery] aircrack-ng not found; skipping key recovery.")
        info.update(
            exit_code=-1,
            stdout="",
            stderr="aircrack-ng not found",
            note="aircrack-ng not installed; key recovery skipped",
        )
        return None, info

    stdout = proc.stdout
    stderr = proc.stderr
    exit_code = proc.returncode

    key_hex = _parse_aircrack_output_for_key(stdout)

    if key_hex:
        print(f"[key_recovery] Key recovered: {key_hex}")
    else:
        print("[key_recovery] No key recovered")

    info.update(
        exit_code=exit_code,
        stdout=stdout,
        stderr=stderr,
    )
    return key_hex, info


def _parse_aircrack_output_for_key(output: str) -> Optional[str]:
    """
    Look for a line like:
      KEY FOUND! [ 12:34:56:78:90 ]
    and return the hex part.
    """
    m = re.search(r"KEY FOUND!\s*\[\s*([0-9A-Fa-f:]+)\s*\]", output)
    if m:
        return m.group(1).lower()
    return None
