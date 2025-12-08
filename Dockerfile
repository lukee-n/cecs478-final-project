FROM python:3.11-slim

# Install system + Python dependencies
RUN apt-get update && \
    apt-get install -y aircrack-ng tcpdump && \
    pip install scapy && \
    rm -rf /var/lib/apt/lists/*

# Work in /app inside the container
WORKDIR /app

# Copy the entire project into the container
COPY . /app/

# Make /app (where src/ lives) importable as a top-level package
ENV PYTHONPATH=/app

# Keep the container running for interactive use
CMD ["tail", "-f", "/dev/null"]
