bootstrap:
	@echo "Setting up environment..."
	docker pull python:3.11-slim
	@echo "Environment ready."

up:
	docker compose up -d --build

demo: up
	docker compose run wep python3 src/demo_pipeline.py data/sample.pcap

run-parser:
	docker compose run wep python3 src/parser.py data/sample.pcap
