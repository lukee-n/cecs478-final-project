bootstrap:
	@echo "Setting up environment..."
	docker pull python:3.11-slim
	@echo "Environment ready."

run-parser:
	docker compose run wep python3 src/parser.py data/sample.pcap
