# Offline WEP Forensics & Key Recovery Pipeline
**CECS 478 Final Project
<br>Luke Nguyen**

A reproducible, Docker-based pipeline for analyzing WEP-encrypted 802.11 traffic, extracting IVs, 
performing offline key-recovery attacks, and generating metrics.

## Features
- Parse PCAP files using Scapy/Pyshark
- Extract WEP IVs and analyze patterns
- Automate FMS/Korek-style key recovery (via Aircrack-ng or custom logic)
- Output metrics: time to crack, packet thresholds, success rate
- Fully reproducible environment using Docker + Makefile

## Requirements
- Docker
- Make

## Quick Start

```bash
make bootstrap
