# Langchain Learning Repository

This is my personal playground for exploring LangChain concepts and implementations using Jupyter notebooks. Expect raw, real-world examples—no fluff.

---

## Project Structure

```
├── 01_talk_with_llm.ipynb             # Basic LLM interaction
├── 02_talk_with_llm2.ipynb            # Refining prompts & handling responses
├── 03_Data_loader_rad_demo.ipynb      # RAG-based data loading/demo
├── 04_RAG_components.ipynb            # Dissecting Retrieval-Augmented Generation
├── 05_Basid_RAG_implementation.ipynb  # Basic RAG pipeline walkthrough
├── 06_LCEL.ipynb                      # LanguageChain Execution Language basics
├── 07_LCEL_Builtin_Runnable.ipynb     # Running built-in Executors via LCEL
├── 08_LCEL_Litte_more.ipynb           # Further LCEL deep dive
├── 09_Memory_langchain.ipynb          # Exploring memory patterns in LangChain
├── demo.py                            # Quick Python demo (CLI or script-based ops)
├── requirements.txt                   # Pin down your dependencies
└── data/                              # Dataset, vectors, or local assets as you're experimenting
```

---

## How to Use This Repo

1. **Clone it locally**
   ```bash
   git clone https://github.com/harsha-chichu/Langchain.git
   cd Langchain
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Dive into the notebooks**
   Launch Jupyter and open the file matching your learning goal:
   - Want to tinker with raw LLM responses? Start with `01_talk_with_llm.ipynb`.
   - Want to build a basic RAG pipeline? Jump to `05_Basid_RAG_implementation.ipynb`.

4. **Run the demo script** (if applicable):
   ```bash
   python demo.py
   ```
   (Add usage instructions here if `demo.py` needs them.)

---

## What You’ll Learn

- How to prompt and interact with LLMs in real time
- How to structure Retrieval-Augmented Generation workflows
- What LCEL is, how executors work, and how to leverage them
- Memory mechanisms within LangChain for more persistent and contextual behavior

---

## Next Steps

- Use this repo as a **playground**, not polished production code. Experiment, break things, and learn.
- Add more notebooks or scripts when you dive into chains, agents, advanced memory systems, or real-world use cases like summarization, user interaction, or API integrations.
- Tidy and refactor as you go—no shame in having messy notebooks during learning, but don’t let that stick around forever.

---

## Feedback and Improvements — Be Blunt

If you stumble on broken code, typos, or misleading assumptions, I want you to call them out—no sugarcoating. That’s how real learning sticks. Feel free to **drop issues**, open PRs, or reach out with anything that’s off.

---

## License

Feel free to copy, share, or break stuff. Just don’t come crying when it goes sideways. Consider this under an MIT license—or whichever you prefer.
