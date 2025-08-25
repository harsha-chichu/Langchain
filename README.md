# LangChain Learning & Experiments

This repository contains my personal notes, experiments, and practice code while learning **LangChain**, **LLMs**, and related AI tools.  
It’s not a production-ready library – just a collection of scripts, prototypes, and examples.

---

## 📂 Repository Structure

- `basics/` – First steps with LangChain (chains, prompts, memory, etc.)
- `agents/` – Experiments with LangChain agents and tools
- `retrieval/` – RAG (Retrieval Augmented Generation) practice
- `streaming/` – Streaming outputs and callback handlers
- `errors/` – Debugging and fixing common LangChain issues
- `notebooks/` – Jupyter/Colab notebooks for step-by-step exploration
- `utils/` – Helper scripts and utilities

> Structure may evolve as I add more examples.

---

## 🚀 Setup

Clone the repo:

```bash
git clone https://github.com/harsha-chichu/Langchain.git
cd Langchain
```

Create a virtual environment & install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

---

## ⚙️ Requirements

- Python 3.10+
- `langchain`
- `openai`
- `chromadb` / `faiss` (for RAG experiments)
- `tiktoken`
- `dotenv`

(See `requirements.txt` for the full list.)

---

## 🔑 Environment Variables

Create a `.env` file in the root with your API keys:

```env
OPENAI_API_KEY=your_key_here
```

---

## 🧪 Running Examples

Each folder contains independent scripts.  
Example:

```bash
python basics/hello_chain.py
```

---

## 📌 Notes

- This repo is **for learning purposes**. Expect rough code, experiments, and trial/error.
- Commits are incremental as I explore new features in LangChain.
- Useful for beginners who want to see raw examples without too much abstraction.

---

## 🛠️ Roadmap

- [ ] Expand RAG examples with vector stores
- [ ] Try LangGraph & CrewAI
- [ ] Add working notebooks with explanations
- [ ] Experiment with multi-agent systems
- [ ] Integrate external APIs/tools

---

## 📜 License

MIT License – free to use and adapt.
