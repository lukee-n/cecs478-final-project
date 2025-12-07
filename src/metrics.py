import os
import json

def save_metrics(metrics: dict, out_dir: str = "artifacts/release/metrics"):
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "metrics.json")

    with open(out_path, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"[metrics] Saved metrics to {out_path}")
