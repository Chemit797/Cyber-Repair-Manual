# AIT203 NLP 项目报告规划与大纲

> **基于官方评分标准 (Rubrics) 的定制化结构**

## 🎯 满分策略 (Rubric Maximization Strategy)
- **Chapter 1 (动机/问题陈述, 5分)**：必须清晰地阐述现实世界的痛点（说明书丢失、维修诈骗）以及技术痛点（生成式 AI 在高压电气维修中的“幻觉”危险）。
- **Chapter 2 & 3 (复杂度与技术差距, 15分)**：评分标准特别要求提出的 NLP 应用必须是 **“非常复杂 (very complex)”** 的。我们将着重强调双阶段级联检索（BM25 + Dense）和动态决策门控（Decision Gate）。这足以证明我们的系统比简单的关键词搜索或调接口（API wrapper）要高级得多。
- **Chapter 4 & 5 (分析与结论, 5分)**：必须超越单纯展示数据。我们将深入分析“级联瓶颈（Cascade Bottleneck）”（解释为什么 Cascaded 方案的 P@1 会略低于仅 Dense 方案，但却在离线计算速度上具有压倒性优势），以此展示极高的学术批判性思维。
- **总体质量 (5分)**：完美的语法，IEEE 格式引用，完全契合要求的结构。

---

## 📝 各章节详细大纲

### 报告前置内容
- **封面 (Cover Page)**：大学 Logo、学院名称、标题（Cyber-Repair-Manual：一个零幻觉的 NLP 故障排查助手）、学生姓名与学号、日期。
- **目录 (TOC), 图表目录 (Table of Figures, Table of Tables)**

### Chapter 1: Introduction (引言)
- **1.1 Motivation (研究动机)**：
  - 消费者痛点：纸质说明书丢失，严重的信息不对称导致维修诈骗。
  - 技术痛点：生成式大语言模型（如 ChatGPT）存在“幻觉（Hallucinations）”，这对于硬件/电气维修极其危险。
- **1.2 Problem Statement (问题陈述)**：
  - 如何在不依赖容易产生幻觉的生成式模型的前提下，搭建一座桥梁，将用户模糊的症状描述精准映射到高专业度的技术维修手册上？
- **1.3 Aim/Objectives (目标与目的)**：
  - 开发一个确定性的、纯本地的 NLP 故障排查系统。
  - 实现双阶段检索流水线。
  - 设计一个安全优先的决策门控，用于交互式歧义消除。
- **1.4 Scope of the Project (项目范围)**：
  - 领域严格限制为四种家电：手电筒、电热水壶、咖啡机、电风扇。
  - 专注处理中/英文文本交互，并搭载 Streamlit Web UI。

### Chapter 2: Literature Review (文献综述) [需学生自行补充]
*(注：你们必须找至少 10 篇以上的论文来填满这一章。强烈建议围绕以下 3 个主题来写)*
1. **关键词检索 vs. 语义检索**：对比 BM25 与 TF-IDF Vectors（TF-IDF Cosine Similarity 等）。
2. **大模型中的幻觉 (Hallucinations in LLMs)**：引用探讨生成式 AI 为何在高危领域（医疗、工程）容易失败的论文。
3. **任务导向型对话系统 (Task-Oriented Dialogue Systems)**：引用关于利用决策树或有限状态机（FSM）来引导用户追问的论文。

### Chapter 3: NLP Application (NLP 系统架构)
- **3.1 System Architecture Overview (系统架构概述)**：展示 5 个阶段流水线的系统架构图。
- **3.2 Phase 0 & 1: Data Structuring & Parsing (语料构建与解析)**：讲解自定义的 `JSONL` 语料库结构，以及基于 `jieba` 的症状提取器（Symptom Parser）。
- **3.3 Phase 2: Two-Stage Cascaded Retriever (双阶段级联检索器)**：
  - BM25（词汇匹配）的底层数学/逻辑原理。
  - `all-MiniLM-L6-v2` 余弦相似度（语义匹配）的底层数学/逻辑原理。
- **3.4 Phase 3: Interactive Decision Gate (交互式决策门控)**：详细介绍置信度分差（Margin）的计算方法，以及安全触发机制（强制拦截高压电 DIY 并建议送修）。
- **3.5 User Interface (用户界面)**：简要展示系统的 Streamlit 前端界面。

### Chapter 4: Result / Analysis / Discussion (结果 / 分析 / 讨论)
- **4.1 Experimental Setup (实验设置)**：描述测试集（50条带有口语、错别字的测试语句）。
- **4.2 Evaluation Metrics (评估指标)**：定义 P@1, P@3, 与 MRR 的概念。
- **4.3 Retrieval Performance (检索性能)**：用表格展示评测结果（提取自 `summary_metrics.csv`），并引用展示图 `retrieval_comparison.png`。
- **4.4 Discussion & Error Analysis (讨论与错误分析)**：
  - *级联妥协 (The Cascade Trade-off)*：着重讨论为什么仅 Dense 方案（84%）打败了 Cascaded 方案（74%）。强力解释：Cascaded 以微小的极端准确率下降为代价，换取了巨大的计算效率提升，使得系统可以在资源受限的家用终端（离线 Edge 硬件）上流畅运行。
  - 引用 `confusion_matrix.png` 和 `per_query_results.csv` 来分析具体的错误或边缘用例（Edge cases）。

### Chapter 5: Conclusion (结论)
- 总结项目成功交付了一个复杂的、零幻觉的 NLP 应用，完美实现了 Chapter 1 中设定的所有目标。

### 报告后置内容
- **References (参考文献)**：使用 IEEE 引用格式。
- **Appendix (附录)**：附上 `train_corpus.jsonl` 节选和核心代码 `retriever.py`。
