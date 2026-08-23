import os
import sys
from pathlib import Path

# Resolve directory paths
repo_root = Path(__file__).resolve().parent
microservices_root = repo_root / "MicroServices"
leadfinder_root = microservices_root / "leadfinder"

for p in [repo_root, microservices_root, leadfinder_root]:
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print(f"[*] Starting LeadFinder FastAPI server on port {port}...")
    uvicorn.run("leadfinder.main:app", host="0.0.0.0", port=port)
