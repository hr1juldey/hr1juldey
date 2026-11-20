# Hrijul Dey

I build agent infrastructure and run it in production. Python, TypeScript, MCP, LLM systems. Thane, India, remote.

**What I do now:** I own the agent platform a 500-person organization runs daily. An MCP gateway over ~480 tool servers — routing, token budgets, failure isolation, evaluation on real traffic. Token cost went down ~93% (15×) while usage went org-wide. Worst-case path: 3 minutes → 30-40 seconds. A later regression to 10-15s went back under 1.5s in ten days.

## Upstream work, Nov 16–20, 2026

I use these tools daily. When they break, I fix them where they live.

- **huggingface/smolagents** — [PR #3206](https://github.com/huggingface/smolagents/pull/3206) merged (token accounting was skipping PlanningStep tokens); parser PR open.
- **NousResearch/hermes-agent** — 5 PRs: credential stores read as plain files, plugin backends reading host files undeclared, a force flag that could skip the terminal safety floor, model-preset caching, cron recovery docs. Found by running the agent on itself, daily.
- **trailhq/Trail-Code** — 13 PRs under review: MCP tool matching, search, guards. Each tied to a filed issue. Tests, CI green.
- **svs/compos** — 2 PRs, 4 issues. **huggingface/tau** — forked, auto-compaction bug reported. **ComposioHQ/composio** — keyword-only tool params, stale API caps.

22 PRs, 6 orgs, 4 days. The week is in the contribution graph; the PRs are in the table below.

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

## My own work

Pinned below. The main one is **[ctx-gateway](https://github.com/hr1juldey/ctx-gateway)** — the gateway pattern I run in production, rebuilt clean-room in public. A benchmark anyone can run: tool-definition payload, task success rate, p95 latency. The build log records what broke and how it got fixed.

Also: **[VerifAI](https://github.com/hr1juldey/VerifAI)** — fraud detection with self-supervised representation learning, precision/recall gates. **[AgentX](https://github.com/hr1juldey/AgentX)** · **[Wapi_bot](https://github.com/hr1juldey/Wapi_bot)** · **[mimicus](https://github.com/hr1juldey/mimicus)** · **[FairWorks_FairDOC](https://github.com/hr1juldey/FairWorks_FairDOC)** · **[dspy-compounding-engineering](https://github.com/hr1juldey/dspy-compounding-engineering)** — older work, kept public.

## Background

Medical and motion AI since 2019 — posture detection, gait analysis, joint loading on CMU motion-capture data. Agents and LLM systems since 2025. Trained small models (16–200 MB) for tool selection inside that platform: shipped, measured, rolled back — below ~500 tools, deterministic routing wins on reward-to-effort. The rollback stays in the story because it was the measurement that mattered.

**Currently:** training a tumor-detection model for a medical-imaging client, and building ctx-gateway's public eval dataset.

I do this work either way. If it is useful to you: **phant0mhriju@gmail.com** · [LinkedIn](https://www.linkedin.com/in/dey-h-ml972) · [GitHub](https://github.com/hr1juldey)
