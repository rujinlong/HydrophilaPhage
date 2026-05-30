# QPROJ Workflow Graph Report

Generated: 2026-05-30 | Project: pc031-aquaPhage | Workflow: analyses | Steps: 4 | Functions: 1 | Tables: 0 | Edges: 3

## For AI assistants -- read this first

This report is the AI navigation entry for the qproj dependency graph.
**Do NOT read `qproj-graph.json` directly** -- it can be 100KB+ on real
projects. Instead, query the graph with the bundled `qg` CLI:

```bash
bash .qproj/graph/qg --help              # full subcommand manual
bash .qproj/graph/qg node <id>           # node metadata + neighbours
bash .qproj/graph/qg impact <id>         # blast radius if you change <id>
bash .qproj/graph/qg deps <id>           # what <id> depends on
bash .qproj/graph/qg unused              # dead code candidates
bash .qproj/graph/qg stale --days 90     # archive candidates
bash .qproj/graph/qg paths <a> <b>       # all dep paths from a to b
```

`qg` only needs `jq` (`brew install jq` / `apt install jq`).
Read `qproj-graph.json` only if `qg` does not surface the field you need.

## Workflow Overview

Pipeline: 111-bacterial_genome -> 112-phage_genome -> 113-tree -> 121-figs

## Step Summary

| Step | Inputs | Upstream Deps | Key Outputs | Notes |
|------|--------|---------------|-------------|-------|
| 111-bacterial_genome | - | none | - | - |
| 112-phage_genome | raw | none | phage_cds.tsv | entry |
| 113-tree | raw | none | TLS_tree.png | entry |
| 121-figs | - | none | fig-combined.png, fig3.png, fig-survival.png | terminal |

## Unused R/ Functions

| Function | Defined |
|---|---|
| `parse_vcontact3()` | R/utils.R:1 |

## How to Use This Graph

- For full dependency details: read `qproj-graph.json`
- For visual exploration: open `qproj-graph.html` in a browser

## AI Navigation Tip

When asked about data flow, check `reads_from` edges in `qproj-graph.json`.
When asked about inputs, check `uses_path_data` / `uses_path_resource` node attributes.
When asked about outputs, check `outputs_detected` node attributes.

