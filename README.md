<div align="center">

<img src="assets/origin_hero.png" alt="Origin Neural AI — Physics-Based Computation at Scale" width="100%">

# Origin Neural AI

### Physics-Based Computation at Scale

[![DSC-3 Isomorphic Engine](https://img.shields.io/badge/DSC--3_Isomorphic_Engine-Live_Demo-red?style=for-the-badge&logo=nvidia&logoColor=white)](https://dsc3.originneural.ai/)
[![Engine API](https://img.shields.io/badge/Engine_API-v1-2196F3?style=for-the-badge&logo=fastapi&logoColor=white)](https://engine.originneural.ai/v1/)
[![Benchmark Paper](https://img.shields.io/badge/D--Wave_Benchmark-DOI-success?style=for-the-badge&logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.20192275)
[![Website](https://img.shields.io/badge/OriginNeural.ai-Platform-blue?style=for-the-badge&logo=safari&logoColor=white)](https://originneural.ai)
[![Blog](https://img.shields.io/badge/Blog-Hashnode-2962FF?style=for-the-badge&logo=hashnode&logoColor=white)](https://originneuralai.hashnode.dev)

[![Spins](https://img.shields.io/badge/500M_spins-21.7s-D4AF37?style=flat-square)](https://dsc3.originneural.ai/)
[![Throughput](https://img.shields.io/badge/Peak-3.63B_ops%2Fsec-FBC15E?style=flat-square)](https://dsc3.originneural.ai/)
[![Ensemble](https://img.shields.io/badge/Solvers-16_cooperative-4878CF?style=flat-square)](https://dsc3.originneural.ai/)
[![Hardware](https://img.shields.io/badge/Hardware-1_GPU-228B22?style=flat-square)](https://dsc3.originneural.ai/)
[![Auth](https://img.shields.io/badge/Auth-Post--Quantum-2196F3?style=flat-square&logo=lock&logoColor=white)](#api-access--security)

---

Conventional solvers hit a wall. Heuristics guess. Brute force runs out of time. Quantum annealers cost millions and cap out at a few thousand qubits.

We took a different path: encode hard problems into physics — spin systems, energy landscapes, spectral geometry — and let a GPU find the answer.

The result is the **DSC-3 Isomorphic Engine**: **half a billion spins solved in 21.7 seconds on a single GPU**, a 16-solver cooperative ensemble that outperforms quantum hardware costing $10M+. It runs live in your browser, ships a documented API, and its central claim — a one-million-spin ground state on a **$1.57/hour** cloud droplet — is published with a DOI, a 40-page paper, and SHA-256-pinned, reproducible artefacts.

**[▶ Try the engine live at dsc3.originneural.ai](https://dsc3.originneural.ai/)**

</div>

---

## Table of Contents

- [The DSC-3 Isomorphic Engine](#the-dsc-3-isomorphic-engine) — the headline result
- [What It Solves](#what-it-solves) — problem classes and live scenarios
- [Live Demo & API Access](#live-demo--api-access) — try it, build on it
- [The D-Wave Benchmark](#the-d-wave-benchmark) — reproducible, DOI-anchored comparison
- [Applications](#applications) — ORIGIN, BioPrime, TopoGrammar, ACO Academy
- [The Stack](#the-stack-physics-to-production) — physics → engine → products
- [Research Program](#research-program) — physics-first, open-verification foundations
- [Principles](#principles) — rigor, reproducibility, falsifiability
- [FAQ](#faq)

---

## The DSC-3 Isomorphic Engine

> **Half a Billion Spins. 21 Seconds. One GPU.**

DSC-3 is a GPU-accelerated combinatorial optimization engine built on **simulated bifurcation** — a classical method rooted in Hamiltonian mechanics where coupled oscillators evolve through adiabatic dynamics to find ground states of Ising spin systems. No quantum hardware required. The physics does the work.

Its defining feature is **isomorphic routing** — the engine maps any incoming problem through the structure-preserving composition **I = F · G · Z₂ · S** onto the solver best suited to its landscape, then runs **16 solvers as a cooperative ensemble** rather than betting on a single heuristic.

| Capability | Performance |
|---|---|
| **Peak scale** | **500,000,000 spins** solved in **21.7 seconds** (single RTX 6000 Ada) |
| **Throughput** | **3.63 billion** spin operations / second (peak ensemble) |
| **Ensemble** | **16 solvers** routed isomorphically and run cooperatively |
| **Connectivity** | Full connectivity — no embedding overhead, no minor-embedding penalty |
| **Hardware** | Commodity NVIDIA GPU — from a $1.57/hour cloud droplet to a ~$5K workstation |
| **Verification** | Headline benchmark blockchain-anchored (BSV) and published with a public DOI |

DSC-3 outscales specialized quantum annealers (D-Wave Advantage2: ~4,400 qubits) by more than **200×** in embeddable problem size while running on hardware that costs four-to-five orders of magnitude less.

**[▶ Run it live](https://dsc3.originneural.ai/)** — interactive solver with Fast / Production / Quality presets and live GPU benchmarks from 1M to 500M spins.

---

## What It Solves

DSC-3 accepts any problem expressible as an Ising / QUBO energy landscape:

| Class | Examples |
|---|---|
| **Core formulations** | Ising model, QUBO, MaxCut, SAT |
| **Routing & assignment** | TSP, supply-chain routing, graph partitioning |
| **Finance** | Portfolio optimization, currency arbitrage |
| **Combinatorial** | Ramsey-type problems, facility location, scheduling |

The live site ships **12 real-world demonstration scenarios** spanning healthcare, finance, logistics, and physics — each runnable in the browser against the production engine.

---

## Live Demo & API Access

| Resource | Link |
|---|---|
| **Interactive engine** | [dsc3.originneural.ai](https://dsc3.originneural.ai/) — Try It Live, 12 scenarios, live 1M–500M benchmarks |
| **Engine API** | [engine.originneural.ai/v1](https://engine.originneural.ai/v1/) — 26 authenticated endpoints |
| **DSC-1 (1M spins)** | [1millionspins.originneural.ai](https://1millionspins.originneural.ai/) — the earlier single-shot demo |

### API Access & Security

| Aspect | Policy |
|---|---|
| **Authentication** | Post-quantum cryptography (Dilithium / ML-DSA) |
| **Endpoints** | 26 authenticated API endpoints; Bearer-token auth |
| **Rate limits** | Per-key concurrency and queue limits |
| **Data retention** | Inputs are not stored. Outputs are blockchain-anchored on request. |
| **Vulnerability reporting** | See `SECURITY.md` |

Request an API key or contact sales from the [live site](https://dsc3.originneural.ai/).

---

## The D-Wave Benchmark

The engine's headline claims are backed by a fully reproducible, peer-style comparison against D-Wave Advantage2 — the only repository in this organization that is **public, open-data, and independently verifiable**.

**[DSC3-DWave-Comparison-2026](https://github.com/OriginNeuralAI/DSC3-DWave-Comparison-2026)** · [DOI: 10.5281/zenodo.20192275](https://doi.org/10.5281/zenodo.20192275) · CC BY 4.0 · 40-page paper · SHA-256 manifest

| Axis | D-Wave Advantage2 | DSC-3 (this work) | Ratio |
|---|---|---|---|
| Max embeddable problem size | 4,400 qubits | **1,000,000** (droplet, n=4 seeds) | ~227× |
| Hardware capex / hourly | $10–15M list | **$1.57/hour** droplet | 10⁴–10⁵× |
| Continuous power | 12.5 kW | 0.30 kW | 42× |
| $/solve at N = 1,728 | $0.05–$1.30 (Leap floor) | **$0.024** | 10²–10⁵× |
| MaxCut Δ vs SA at N = 10,000 | not embeddable | **+0.13–0.20%**, σ ≤ 0.02% | DSC-3 only |

Every numerical claim traces to a `results/*.json` file with a SHA-256 digest pinned in the paper. The same engine on a $700 consumer Blackwell card reproduces droplet results to within FP32 noise.

---

## Applications

The same physics-based core powers a family of production platforms:

| Platform | Domain | Key Metric | Link |
|---|---|---|---|
| **ORIGIN Voice** | AI voice synthesis | Real-time streaming, voice cloning, free | [originneural.ai](https://originneural.ai) |
| **BioPrime v4.0** | Drug discovery | 45% accuracy gain, R² = 0.73 across 10 targets | [bioprime.one](https://bioprime.one) |
| **TopoGrammar** | 3D genomics | VUS reclassification 93%, F1 = 0.91 | [topogrammar](https://topogrammar.e2multipass.com) |
| **ACO Academy** | Agentic commerce | 7-layer optimization stack + [benchmark tool](https://agenticcommerce.academy/benchmark) | [agenticcommerce.academy](https://agenticcommerce.academy/) |

---

## The Stack: Physics to Production

```
 PHYSICS                  ENGINE                    PRODUCTS
 ───────                  ──────                    ────────
 Ising Model       ──>    DSC-3 Isomorphic   ──>    Optimization (500M spins)
 Hamiltonian Dynamics      Engine                    Drug Discovery (BioPrime)
 Simulated Bifurcation     (I = F·G·Z₂·S            Genomics (TopoGrammar)
 Spectral Geometry          isomorphic routing,      Voice Synthesis (ORIGIN)
 Statistical Mechanics      16-solver ensemble)      Agentic Commerce (ACO)
```

---

## Research Program

Origin Neural's engine sits on a deep physics-first research foundation: **31 papers, 500+ computational verification checks, zero falsifications**, with results timestamped and permanently anchored to the BSV blockchain for immutable, publicly verifiable provenance.

This research portfolio is maintained under proprietary access. Selected work is published openly — including the [D-Wave benchmark](https://github.com/OriginNeuralAI/DSC3-DWave-Comparison-2026) (DOI, CC BY 4.0) — and ongoing results are written up on the [blog](https://originneuralai.hashnode.dev). For academic verification, collaboration, or licensing inquiries, reach us via [originneural.ai](https://originneural.ai).

---

## Principles

**Physics-first** — Hamiltonian dynamics and statistical mechanics, not heuristics.

**Rigor over hype** — Null results reported alongside confirmations.

**Open verification** — Our headline benchmark is fully public, DOI-anchored, and reproducible from SHA-256-pinned data.

**Falsifiability** — Claims are stated so they can be checked. Reproduction scripts ship with the public benchmark.

**Security** — Post-quantum auth on all APIs. Vulnerability reporting via `SECURITY.md`. No security through obscurity.

---

## FAQ

<details>
<summary><strong>What is the DSC-3 Isomorphic Engine?</strong></summary>
<br>

A GPU-accelerated optimization engine based on **simulated bifurcation** — a classical physics method rooted in Hamiltonian mechanics. Coupled oscillators evolve through adiabatic dynamics to find ground states of Ising spin systems. Its **isomorphic router** (I = F·G·Z₂·S) maps each problem onto the best-suited solver and runs 16 solvers as a cooperative ensemble. It solves up to 500M-spin problems in seconds on a single commodity NVIDIA GPU. No quantum hardware required.

</details>

<details>
<summary><strong>How can I verify your claims?</strong></summary>
<br>

Our headline benchmark is fully public. Clone [DSC3-DWave-Comparison-2026](https://github.com/OriginNeuralAI/DSC3-DWave-Comparison-2026), check every datapoint against the SHA-256 manifest in the paper, and re-run the pipeline yourself (`sha256sum results/*.json`, then `aggregate_results.py` / `make_plots.py`). The repository is CC BY 4.0 and carries a DOI. You can also run the engine directly at [dsc3.originneural.ai](https://dsc3.originneural.ai/).

</details>

<details>
<summary><strong>How does DSC-3 compare to D-Wave?</strong></summary>
<br>

On every fully-connected MaxCut cell we measured up to N = 10,000 vertices — over 2× past D-Wave Advantage2's 4,400-qubit embedding ceiling — DSC-3 beats matched-compute simulated annealing by many standard deviations, while running on hardware that costs 4–5 orders of magnitude less and draws ~42× less power. Full table and methodology are in the [benchmark repository](https://github.com/OriginNeuralAI/DSC3-DWave-Comparison-2026).

</details>

<details>
<summary><strong>What does "blockchain-anchored" mean?</strong></summary>
<br>

Headline results and papers are timestamped and permanently recorded on the BSV blockchain. This provides immutable, publicly verifiable proof of when a result was produced — preventing after-the-fact modification. Anyone can verify the timestamp via the transaction ID without our permission or tools.

</details>

<details>
<summary><strong>Why report null results?</strong></summary>
<br>

Science requires falsifiability. We report what doesn't work alongside what does — it builds trust and helps others avoid dead ends.

</details>

---

<div align="center">

<img src="assets/origin_logo_icon.png" alt="Origin Neural AI" width="48">

[DSC-3 Engine](https://dsc3.originneural.ai/) | [Engine API](https://engine.originneural.ai/v1/) | [D-Wave Benchmark](https://github.com/OriginNeuralAI/DSC3-DWave-Comparison-2026) | [OriginNeural.ai](https://originneural.ai) | [BioPrime](https://bioprime.one) | [TopoGrammar](https://topogrammar.e2multipass.com) | [ACO Academy](https://agenticcommerce.academy/) | [Blog](https://originneuralai.hashnode.dev)

**Origin Neural AI** — Research + Engineering

*Physics-based computation. Real systems. Open science.*

</div>
