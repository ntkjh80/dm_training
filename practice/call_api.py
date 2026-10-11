"""Call the local Unsloth Decision API. No third-party packages needed."""
import argparse
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--request", type=Path, default=Path(__file__).with_name("request.json"))
    p.add_argument("--port", type=int, default=8888)
    args = p.parse_args()
    payload = json.loads(args.request.read_text(encoding="utf-8-sig"))
    headers = {"Content-Type": "application/json"}
    token = os.environ.get("UNSLOTH_API_KEY")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(
        f"http://127.0.0.1:{args.port}/v1/systemone",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers=headers, method="POST")
    try:
        # Bypass proxy variables for this deliberately local-only example.
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        with opener.open(request, timeout=300) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"Local API unavailable: {exc.reason}. Check Studio and Decision API settings.")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    team = result.get("answers", {}).get("team", {})
    probabilities = team.get("probabilities", {})
    # This is a teaching threshold, not one validated for your workflow.
    if probabilities:
        selected = max(probabilities, key=probabilities.get)
        print("Example routing:", selected if probabilities[selected] >= 0.8 else "human_review")

if __name__ == "__main__":
    main()
