#!/usr/bin/env python3
"""Refresh the ACTIVITY table in README.md from GitHub Search API (no deps)."""
import json, os, re, sys, urllib.request

USER = "hr1juldey"
TOKEN = os.environ.get("GH_TOKEN", "")
Q = f"https://api.github.com/search/issues?q=author:{USER}+type:pr+-user:{USER}&sort=updated&order=desc&per_page=12"

req = urllib.request.Request(Q, headers={
    "Accept": "application/vnd.github+json",
    "User-Agent": "profile-activity",
    **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.load(r)

rows = ["| Repo | Pull request | State | Updated |", "|---|---|---|---|"]
for it in data.get("items", []):
    repo = it["repository_url"].rsplit("/", 1)[-1]
    if it.get("pull_request", {}).get("merged_at"):
        state = "**merged**"
    else:
        state = it["state"]
    updated = it["updated_at"][:10]
    rows.append(f"| {repo} | [{it['title'][:70]}]({it['html_url']}) | {state} | {updated} |")

table = "\n".join(rows) if len(rows) > 2 else "_No upstream pull requests found._"
body = "\n<!--ACTIVITY:START-->\n_Recent pull requests in other people's repositories (auto-updated daily):_\n\n" + table + "\n<!--ACTIVITY:END-->\n"

path = os.path.join(os.path.dirname(__file__), "..", "README.md")
readme = open(path).read()
new = re.sub(r"<!--ACTIVITY:START-->.*?<!--ACTIVITY:END-->", body.strip(), readme, flags=re.S)
if new == readme:
    print("no change"); sys.exit(0)
open(path, "w").write(new)
print(f"activity table refreshed: {len(rows)-2} PRs")
