# Cyber Threat Detection System

> A comparative ML/DL threat classification system grounded in KDD99 attack signatures, with a forward-looking architecture for RAG-augmented threat intelligence.

---

## Overview

This system detects and classifies network intrusions using seven machine learning and deep learning algorithms trained on the KDD Cup 1999 dataset — the standard benchmark for intrusion detection research. Beyond classification, it generates analyst-readable **Threat Intelligence Briefs** for each detected attack class, simulating the output of a Retrieval-Augmented Generation (RAG) pipeline.

---

## System Architecture

![Architecture Diagram](SOURCE%20CODE/CyberThreat/assets/architecture.png)

The system operates in two layers:

**Detection Layer** — Seven models (LSTM, DNN, SVM, KNN, Random Forest, Naive Bayes, Decision Tree) are trained and evaluated in parallel. TF-IDF preprocessing converts raw network feature vectors into a representation suitable for multi-class classification. A structured metrics dashboard compares Accuracy, Precision, Recall, and F1-Score across all models.

**Intelligence Layer** — When a threat is detected, the system maps the predicted class to a structured knowledge base of MITRE ATT&CK entries, severity ratings, network indicators, and remediation steps. This layer simulates what a production RAG pipeline would do: retrieve relevant CVE/ATT&CK documents and generate an analyst-readable brief.

---

## Use Case Diagram

![Use Case Diagram](SOURCE%20CODE/CyberThreat/assets/usecase.png)

---

## Algorithms Compared

| Model | Type | Notes |
|-------|------|-------|
| LSTM | Deep Learning (RNN) | Sequential pattern recognition |
| DNN | Deep Learning (Feedforward) | Dense multi-layer classifier |
| SVM | Classical ML | Linear kernel, C=2.0 |
| KNN | Classical ML | k=10 neighbors |
| Random Forest | Ensemble | 5 estimators |
| Naive Bayes | Probabilistic | BernoulliNB |
| Decision Tree | Classical ML | Entropy, max_depth=3 |

---

## Dataset: KDD Cup 1999

- **41 features** — network timing, traffic metrics, login attempts, host statistics
- **18 threat classes** — DoS, Probe, U2R, R2L, and normal traffic
- **20,000 records** — 10,000 training / 10,000 testing
- **Source:** [KDD Cup 1999 Data](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

---

## Threat Intelligence Brief (Simulated RAG Output)

After any model run, clicking **Generate Threat Brief** produces structured intelligence per detected threat class:

```
[THREAT DETECTED] NEPTUNE (DoS)
─────────────────────────────────────────────────────
Description:     SYN flood attack exhausting the TCP half-open connection queue
MITRE ATT&CK:    T1498.001 - Direct Network Flood
Severity:        HIGH
Indicators:      High SYN rate, low ACK ratio, serror_rate > 0.9
Recommended:     Enable SYN cookies, rate-limit inbound SYN packets
─────────────────────────────────────────────────────
```

---

## Relationship to RAG Architecture

This system's knowledge architecture maps directly to a RAG pipeline:

| RAG Component | This System's Equivalent |
|---------------|--------------------------|
| Document corpus | KDD99 labeled attack records |
| Embedding + vector index | TF-IDF vectorization |
| Retrieval step | ML model inference (nearest class) |
| LLM-generated answer | Threat Intelligence Brief (template KB) |
| Non-parametric knowledge | MITRE ATT&CK / CVE templates |

**The natural production evolution:** Replace the template KB with a vector database of CVE reports and MITRE ATT&CK entries. At inference time, embed the detected threat class, retrieve top-k relevant documents, and pass them to an LLM to generate a fully grounded, citable threat brief — enabling a true Detect → Retrieve → Explain pipeline.

---

## Setup & Run

```bash
pip install -r "SOURCE CODE/CyberThreat/requirements.txt"
python "SOURCE CODE/CyberThreat/CyberThreatDetection.py"
```

To regenerate diagrams:
```bash
python "SOURCE CODE/CyberThreat/diagrams.py"
```

---

## Workflow

1. **Upload Train Dataset** — Load `kdd_train.csv`
2. **Run Preprocessing** — Apply TF-IDF feature extraction
3. **Generate Event Vector** — Create 80/20 train/test split
4. **Neural Network Profiling** — Train LSTM and DNN
5. **Run individual models** — SVM, KNN, RF, NB, DT
6. **Generate Threat Brief** — View analyst-readable intelligence
7. **Comparison Graphs** — View Accuracy / Precision / Recall / F1 charts
## Prerequisites

- Python 3.8+
- TensorFlow / Keras
- scikit-learn
- pandas, numpy
- matplotlib

## License

MIT License
