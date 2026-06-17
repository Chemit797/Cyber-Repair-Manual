# Cyber-Repair-Manual
[English](README.md) | [中文](README_zh.md)

A Hallucination-Free, Fair-Repair Assistant for Home Appliances.

## Introduction
When home appliances break, users often face lost manuals and information asymmetry. General AI models tend to hallucinate, which introduces significant risks in high-voltage appliance repairs.

Cyber-Repair-Manual is a deterministic, offline troubleshooting assistant. It relies strictly on curated instruction manuals and expert repair corpora. It acts as an interactive manual to prevent repair scams without the risks of generative AI hallucinations.

## Core Mechanics
- **Zero Hallucination**: Answers are extracted from verified instruction manuals via semantic retrieval.
- **Anti-Scam & Safety Protocol**: Distinguishes between DIY fixes and hardware faults. High-voltage issues trigger a hard stop advising professional repair.
- **Two-Stage Cascaded Retrieval**: 
  1. Lexical Recall (`rank_bm25`)
  2. Dense Reranking (`sentence-transformers` / Cosine Similarity)
- **Interactive Decision Gate**: Ambiguous inputs trigger targeted clarification questions based on data-driven decision trees.
- **100% Offline**: Runs entirely locally. No external API dependencies.

## Architecture
- **Phase 0 - The Cyber Corpus**: Manuals structured into a JSONL schema covering symptoms, safety notes, and atomic steps.
- **Phase 1 - Symptom Parser**: Utilizes `jieba` to extract target devices and symptom keywords.
- **Phase 2 - Retriever**: Device Hard Filter -> BM25 Recall -> Dense Embedding Reranking.
- **Phase 3 - Decision Gate**: Evaluates confidence margin. Low confidence triggers dynamic clarification.
- **Phase 4 - Renderer**: Formats retrieved manual entries into structured Markdown output.

## Visuals
![System Preview](web.png)

## Execution Examples

**[Case 1: High Confidence]**
- Input: "The light keeps flickering, sometimes bright sometimes dim"
- Output: 
  - Diagnosis: Dim or flickering (Severity: DIY Repair)
  - Steps: 1. Replace with fully charged batteries... 2. Clean contacts with an alcohol swab...

**[Case 2: Safety Protocol Triggered]**
- Input: "My kettle is leaving a puddle on the table and dripping constantly"
- Output: 
  - WARNING: Beyond DIY repair. Safety risks involved.
  - Notes: Unplug immediately! Water leaking onto the high-voltage base is a severe electrocution hazard!

**[Case 3: Clarification Gate]**
- Input: "Pump is loud but no coffee comes out"
- Internal State: Low confidence margin detected.
- System Prompt: "Did the water tank recently run completely dry before this started happening?" (Awaiting Yes/No from user to rerank candidates).

## Getting Started

**Requirements**: Python 3.10+

**1. Clone repository**
```bash
git clone https://github.com/Chemit797/Cyber-Repair-Manual.git
cd Cyber-Repair-Manual
```

**2. Setup Environment**

Windows:
```powershell
.\setup.ps1
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Cache Embedding Model**
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

## Usage
Launch Web UI:
```bash
streamlit run app.py
```

Test backend logic via terminal:
```bash
python test_run.py
```

## Credits
Developed for the AIT203 Natural Language Processing course group project. The project explores addressing hallucination in generative AI within high-stakes domains via retrieval and symbolic logic.
