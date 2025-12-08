# Offline WEP Forensics & Key Recovery Pipeline
**CECS 478 Final Project
<br>Luke Nguyen**

A reproducible, Docker-based pipeline for analyzing WEP-encrypted 802.11 traffic, extracting IVs, 
performing offline key-recovery attacks, and generating metrics. [Demo](https://youtu.be/8dGqVixl5js)

## Features
- PCAP parsing using Scapy
- WEP IV extraction and packet analysis
- Automated key recovery via Aircrack-ng (FMS/Korek/PTW attacks)
- Metrics output: packet count, IV count, runtime, recovered key
- Artifacts saved under artifacts/release/ (metrics + logs)
- Fully reproducible Docker environment
- Makefile targets for up, demo, bootstrap
- Automated tests + GitHub Actions CI

## Requirements
- Docker Desktop or Docker Engine
- Make
- (For local testing only) Python 3.10+ and pip

## Installation (WSL / Linux / MacOS)
```bash
git clone https://github.com/lukee-n/cecs478-final-project.git
cd cecs478-final-project.git
make bootstrap
```
## Quick Start (Vertical Slice Demo)
This runs the end-to-end WEP forensics pipeline inside Docker.
```bash
make up
make demo
```
This performs:
1. Parse PCAP (data/sample.pcap)
2. Extract WEP IVs
3. Run Aircrack-ng for key recovery
4. Generate metrics (JSON)
5. Save logs and artifacts

## Output Artifacts

### Metrics JSON:
artifacts/release/metrics/metrics.json

Example fields:
{
  "pcap": "data/sample.pcap",
  "packet_count": 65282,
  "iv_count": 30630,
  "key_recovered": true,
  "recovered_key": "1f:1f:1f:1f:1f",
  "elapsed_seconds": 10.44,
  "command": "aircrack-ng data/sample.pcap",
  "exit_code": 0
}

### Log File:
artifacts/release/logs/pipeline.log
Contains all pipeline log messages captured via log().

## Testing
To run tests locally (outside Docker):

pip3 install -r requirements.txt
python3 -m pytest

Tests include:
- Happy-path: pipeline produces metrics.json
- Negative: missing PCAP raises FileNotFoundError
- Edge-case tests for IV extraction and key recovery

## CI
GitHub Actions automatically:
- Installs dependencies
- Runs pytest
- Shows coverage summary

Check the Actions tab in your repository.

## Evaluation Datasets
Place multiple WEP capture files in the data/ directory.

Example:
docker compose run wep python3 src/demo_pipeline.py data/wep_big.pcap
cp artifacts/release/metrics/metrics.json artifacts/release/metrics/metrics_wep_big.json

You can evaluate:
- IV count
- time to crack
- packet thresholds
- comparison between datasets

## Security Invariants
- Only PCAPs in data/ are processed
- No live capture; offline analysis only
- Recovered keys stored in metrics but not printed in logs unless needed
- Containerized environment prevents host modification
- All artifacts written under artifacts/release/

## What Works
- Full end-to-end WEP forensics pipeline
- Successful key recovery on real WEP captures
- Metrics + logs saved consistently
- Tests + CI passing
- Docker-based reproducibility using make up && make demo

## What’s Next
- Batch-mode pipeline for multiple PCAPs
- Metrics visualization (charts)
- Additional hardening
- More negative/edge tests
