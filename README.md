# 🐳 Multistager

**Multistager** is a Python CLI tool that automatically converts single-stage Dockerfiles into optimized multi-stage Dockerfiles. It uses heuristics and regex-based classification to detect build instructions, runtime instructions, and build artifacts.

---

## 🚀 Features

- 🔍 Parses Dockerfiles into structured instructions
- 🧠 Classifies instructions as build-stage or runtime
- 🛠️ Supports popular runtimes like **Node.js** and **Python**
- 📦 Outputs a clean, efficient multistage Dockerfile
- 🧪 Includes debug and quiet modes

---

## 📦 Installation

### ▶️ Option 1: Install from source

```bash
git clone https://github.com/yourname/multistager.git
cd multistager
pip install -e .
