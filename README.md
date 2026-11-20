# Hrijul Dey

![Python](https://img.shields.io/badge/Python-production%20daily-3776AB?logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-13%20open%20PRs-3178C6?logo=typescript&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-in%20production-8A2BE2)
![LLM systems](https://img.shields.io/badge/LLM%20systems-agent%20infra-FF6F00)
![Location](https://img.shields.io/badge/location-Thane%2C%20India%20%C2%B7%20remote-success)

I build agent infrastructure and run it in production. Day job: the agent platform a 500-person organization runs daily — an MCP gateway over ~480 tool servers. Routing, token budgets, failure isolation, evaluation on real traffic. Token cost went down ~93% (15×) while usage went org-wide. Worst-case path: 3 minutes → 30-40 seconds; a later regression went back under 1.5s in ten days.

The rest of this page is my own work. Everything linked is public and runnable.

## Personal projects

| Project | What it is | Status |
|---|---|---|
| [ctx-gateway](https://github.com/hr1juldey/ctx-gateway) | The gateway pattern from my day job, rebuilt clean-room in public. Capability registry, per-task tool-subgraph routing, token budgets, failure isolation. Benchmark anyone can run: tool-definition payload, task success rate, p95 latency. Build log records what broke. | active — benchmark live, eval dataset in progress |
| [VerifAI](https://github.com/hr1juldey/VerifAI) | Fraud detection with self-supervised representation learning (JEPA-class). Precision/recall gates, not vibes. | active |
| [openpencil](https://github.com/hr1juldey/openpencil) | Open-source AI-native vector design tool — concurrent agent teams drawing on one live canvas. Design-as-code. | prototype |
| [AgentX](https://github.com/hr1juldey/AgentX) | Agent-system experiments: 77 commits of planning loops, tool use, multi-agent patterns. | experiments |
| [Wapi_bot](https://github.com/hr1juldey/Wapi_bot) | WhatsApp booking assistant — FastAPI backend, rule-based workflows plus learned planning. | shipped |
| [FairWorks_FairDOC](https://github.com/hr1juldey/FairWorks_FairDOC) | Healthcare documentation workflows for medical professionals. | 90+ commits |
| [dspy-compounding-engineering](https://github.com/hr1juldey/dspy-compounding-engineering) | Local-first AI engineering agent that learns from your codebase (DSPy). | experiment |
| [mimicus](https://github.com/hr1juldey/mimicus) | MCP-integrated agent system. | experiment |
| [omen](https://github.com/hr1juldey/omen) | Scene-aware JEPA render accelerator — research rendering engine. | research |

Older and smaller things stay public too. Work is work.

## Upstream contributions

I use these tools daily. When they break, I fix them where they live. Between **Nov 16–20, 2026**: 22 PRs across 6 orgs.

- **huggingface/smolagents** — [PR #3206](https://github.com/huggingface/smolagents/pull/3206) merged (token accounting was skipping PlanningStep tokens); parser PR open.
- **NousResearch/hermes-agent** — 5 PRs: credential stores read as plain files, plugin backends reading host files undeclared, a force flag that could skip the terminal safety floor, model-preset caching, cron recovery docs. Found by running the agent on itself, daily.
- **trailhq/Trail-Code** — 13 PRs under review: MCP tool matching, search, guards. Each tied to a filed issue. Tests, CI green.
- **svs/compos** — 2 PRs, 4 issues · **huggingface/tau** — forked, auto-compaction bug reported · **ComposioHQ/composio** — keyword-only tool params, stale API caps.

<!--ACTIVITY:START-->
_Recent pull requests in other people's repositories (auto-updated daily):_

| Repo | Pull request | State | Updated |
|---|---|---|---|
| hermes-agent | [fix(vision): read host files for plugin backends that declare uses_hos](https://github.com/NousResearch/hermes-agent/pull/158144) | open | 2026-11-20 |
| hermes-agent | [fix(redact): treat Hermes-home credential stores as secret-file reads](https://github.com/NousResearch/hermes-agent/pull/158145) | open | 2026-11-20 |
| hermes-agent | [fix(terminal): run the hardline floor even when force=True](https://github.com/NousResearch/hermes-agent/pull/158143) | open | 2026-11-20 |
| smolagents | [DuckDuckGo parser: discard incomplete record when a new result starts](https://github.com/huggingface/smolagents/pull/3227) | open | 2026-11-20 |
| smolagents | [Monitor: include PlanningStep tokens in monitor totals (Fixes #3187)](https://github.com/huggingface/smolagents/pull/3206) | **merged** | 2026-11-20 |
| hermes-agent | [fix(caching): family-match @preset models on their resolved head model](https://github.com/NousResearch/hermes-agent/pull/158147) | open | 2026-11-20 |
| hermes-agent | [docs(cron): correct the interrupted-run recovery paragraph](https://github.com/NousResearch/hermes-agent/pull/158146) | open | 2026-11-20 |
| compos | [chat: agent-switch offers what the connector backend reported](https://github.com/svs/compos/pull/19) | open | 2026-11-20 |
| compos | [hotload: a backend that ignores keeps the daemon up](https://github.com/svs/compos/pull/20) | open | 2026-11-20 |
| Trail-Code | [fix(lock): a dead pid loses its lock immediately, not after five minut](https://github.com/trailhq/Trail-Code/pull/861) | open | 2026-11-19 |
| Trail-Code | [fix(upkeep): one background helper per window, not one per process (#8](https://github.com/trailhq/Trail-Code/pull/859) | open | 2026-11-19 |
| Trail-Code | [fix(claude): tool-savings PostToolUse matcher never matches MCP tools](https://github.com/trailhq/Trail-Code/pull/850) | open | 2026-11-19 |
<!--ACTIVITY:END-->

## Background

Medical and motion AI since 2019 — posture detection, gait analysis, joint loading on CMU motion-capture data. Agents and LLM systems since 2025. Along the way I trained small models (16–200 MB) for tool selection: shipped, measured, rolled back — below ~500 tools, deterministic routing wins on reward-to-effort. The rollback stays in the story because it was the measurement that mattered.

**Currently:** training a tumor-detection model for a medical-imaging client, and building ctx-gateway's public eval dataset.

**How I work:** every system gets a gate that can fail and a number that can be read. Measured, not felt.

I do this work either way. If it is useful to you: **phant0mhriju@gmail.com** · [LinkedIn](https://www.linkedin.com/in/dey-h-ml972) · [GitHub](https://github.com/hr1juldey)
