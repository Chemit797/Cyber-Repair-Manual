# Cyber-Repair-Manual 📖⚡
> **"赛博说明书" —— The Hallucination-Free, Fair-Repair Assistant for Home Appliances**

---

## 💡 Why This Project? (为什么做这个项目？)

When home appliances break, users face two major pain points:
1. **Lost Manuals**: Paper manuals are always lost when you actually need them.
2. **The "Repair Scam"**: Without knowing the real issue, users are easily overcharged by rogue repair services for minor faults.

While general AI (like ChatGPT) can answer repair questions, **they hallucinate**. In appliance repair, hallucinating a step involving high voltage can be catastrophic. 

**Cyber-Repair-Manual (赛博说明书)** is built differently. It is **NOT** a generative black box. It is a strictly deterministic, interactive tool driven entirely by a highly curated corpus of actual **instruction manuals and expert repair logic**. It acts as your reliable "Cyber Manual"—guaranteeing zero hallucinations and empowering you with the exact truth of your appliance's fault so you are never scammed again.

日常生活中，一旦家电出毛病，我们往往面临两个绝望的瞬间：“纸质说明书早找不到了”和“不懂行，怕被维修师傅当肥羊宰”。虽然现在可以直接去问通用大模型（如 ChatGPT），但在维修领域，**大模型会产生“幻觉”**，这在涉及强电排查时是极其危险的。

本项目正为此而生。**我们不凭空生成答案，我们只做说明书的“智能搬运工”。** 所有的回答100%基于人工精编的官方说明书与权威维修语料库，实现绝对的**“零幻觉”**。它是一份听得懂大白话的“赛博说明书”，不仅手把手教你安全地 DIY 解决小毛病，更让你在面对维修工时底气十足，拒绝被坑（Fair Repair）！

---

## ✨ Core Features (核心特性)

- 🚫 **Zero Hallucination (绝对零幻觉)**: Answers are purely extracted from verified instruction manual corpora using Semantic Retrieval. No generative guesswork.
- 🛡️ **Anti-Scam & Safety-First (防坑与绝对安全)**: Clearly identifies minor DIY fixes versus major hardware faults. If it's a high-voltage issue, it triggers a hard stop, advising professional repair to keep you safe and informed.
- 🔍 **Two-Stage Cascaded Retrieval (双阶段级联检索)**: 
  - *Recall*: `rank_bm25` for lexical matching.
  - *Reranking*: `sentence-transformers` for deep semantic matching (Cosine Similarity).
- 🌳 **Interactive Clarification (交互式防误判)**: When your symptoms are vague, the system asks targeted questions from its decision tree to pinpoint the exact issue, just like a real diagnostic manual.
- 🔒 **100% Offline (纯本地运行)**: Runs locally without any external API dependencies. 

---

## 🏗️ System Architecture (系统架构)

1. **Phase 0 - The Cyber Corpus (说明书重构)**: Real manuals are broken down into a strictly defined JSONL schema (symptoms, safety notes, atomic steps).
2. **Phase 1 - Symptom Parser**: Uses `jieba` to extract target devices and symptom keywords from colloquial user input.
3. **Phase 2 - Retriever**: Device Hard Filter -> BM25 Top-10 Recall -> Dense Embedding Top-K Reranking.
4. **Phase 3 - Decision Gate**: Evaluates exact match confidence. Ambiguous inputs trigger a dynamic clarification question.
5. **Phase 4 - Renderer**: Converts the retrieved manual entry into a structured, highly readable Markdown troubleshooting guide.

---

## 🚀 Quick Start (快速上手)

### Prerequisites (环境要求)
- Python 3.10+

### Installation (安装与配置)

**1. Clone the repository**
```bash
git clone https://github.com/your-username/Cyber-Repair-Manual.git
cd Cyber-Repair-Manual
```

**2. Setup Virtual Environment & Install Dependencies**

For Windows (using provided PowerShell script):
```powershell
.\setup.ps1
```

For Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**3. Cache the Embedding Model**
To guarantee offline capabilities (perfect for live demos), cache the dense model locally:
```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"
```

### Usage (运行系统)

Launch the interactive Web UI:
```bash
streamlit run app.py
```
Open your browser and type in your colloquial appliance issue (e.g., "My coffee machine is leaking from the bottom"). The Cyber Manual will retrieve the exact official step to guide you.

---

## 📚 Academic Context

Developed for the **AIT203 Natural Language Processing** course group project. This project demonstrates how to build a highly reliable, domain-specific NLP application using retrieval and symbolic logic, directly solving the hallucination problem prevalent in modern generative AI within high-stakes domains like appliance repair.
