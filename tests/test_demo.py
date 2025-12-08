import json
import os
from pathlib import Path
import shutil

import pytest

import src.demo_pipeline as demo
from src.iv_extraction import extract_ivs
from src.key_recovery import recover_key_from_pcap


ARTIFACTS_DIR = Path("artifacts/release/metrics")
METRICS_PATH = ARTIFACTS_DIR / "metrics.json"


def _clean_metrics_dir():
    if ARTIFACTS_DIR.exists():
        shutil.rmtree(ARTIFACTS_DIR, ignore_errors=True)


def test_demo_creates_metrics():
    """
    Happy-path test:
    Run the demo on data/sample.pcap.
    Expect metrics.json to be created with some basic fields.
    """
    _clean_metrics_dir()
    assert Path("data/sample.pcap").exists()

    # Run the full pipeline
    demo.main()

    assert METRICS_PATH.exists(), "metrics.json was not created"

    data = json.loads(METRICS_PATH.read_text())
    assert data["pcap"] == "data/sample.pcap"
    assert "packet_count" in data
    assert "iv_count" in data
    assert "key_recovered" in data


def test_missing_pcap_raises(monkeypatch):
    """
    Negative test:
    If we point demo at a non-existent PCAP, it should raise FileNotFoundError.
    """
    # Override argv inside demo module
    monkeypatch.setattr(
        demo.sys,
        "argv",
        ["demo_pipeline.py", "data/does_not_exist.pcap"],
    )

    with pytest.raises(FileNotFoundError):
        demo.main()


def test_extract_ivs_empty_list():
    """
    Edge-case test:
    extract_ivs() should handle an empty packet list and return an empty list.
    """
    ivs = extract_ivs([])
    assert ivs == []


def test_recover_key_from_pcap_missing_file():
    """
    Edge-case test for recover_key_from_pcap:
    Missing pcap path should raise FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        recover_key_from_pcap("data/no_such_file.pcap")
