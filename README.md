# SOP Troubleshooting Assistant

<p align="center">
  <img src="https://github.com/abedy101/sop-troubleshooting-assistant/blob/main/assets/scrn3.png?raw=true" alt="SOP App Screenshot" width="720"/>
</p>

An AI-powered assistant that allows users to **ask questions about any SOP, user manual, or document**, and instantly get context-aware answers — powered by GPT and vector search.

No more keyword guessing or manual scrolling through pages. Just ask, and get the exact steps, policies, or procedures — from your own document.

---

## Key Features

- RAG pipeline using LangChain + GPT-4
- Preloaded PDF document (`example.pdf`)
- FAISS-based semantic search with auto chunking
- Automatic index rebuild when PDF changes (via hashing)
- Clean Streamlit UI with context caption
- Blazing-fast query time after initial indexing

---

## Demo Document: iPhone User Guide

This demo loads Apple’s iPhone User Guide to simulate a real-world SOP.

### Try Asking:

- “Why is my battery draining too fast?”
- “How do I restart my iPhone?”
- “How do I back up to iCloud?”
- “How can I turn on Face ID?”

---

## Real Use Case Examples

This assistant can be customized to handle:

-  **Customer support**: returns, refunds, troubleshooting
-  **Company SOPs**: onboarding, compliance, security
-  **Manufacturing**: machine reset steps, error codes
-  **IT support**: network protocols, service tickets
-  **HR documents**: employee leave, benefits, training
-  **Student handbooks**: university helpdesks, rules

---

## How to Run It Locally

1. Clone the repo  
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Add your OpenAI key to a `.env` file:

    ```env
    OPENAI_API_KEY=your_openai_key
    ```

4. Place your PDF inside `data/` folder and rename it to `example.pdf`

5. Launch the app:

    ```bash
    streamlit run app.py
    ```

Done. The assistant will auto-index your document the first time you run it, and re-index if you change the file later.

---

## 📁 Project Structure

```
sop-troubleshooting-assistant/
├── app.py                  ← Streamlit UI
├── rag_engine.py           ← RAG logic + auto-indexing
├── utils/pdf_loader.py     ← PDF parsing + chunking
├── data/example.pdf        ← Your input document
├── vector_store/           ← FAISS index (auto-generated)
├── requirements.txt
├── .env                    ← Your OpenAI key (not tracked by Git)
└── assets/scrn3.png        ← UI screenshot
```

---

## 🔄 Future Upgrades

- Upload any PDF directly from Streamlit
- Show matched paragraph source in the UI
- Export answers to `.txt` or copy-to-clipboard
- Handle multiple SOPs at once
- Deploy on Hugging Face or Streamlit Cloud

---

## Contact

Made by [@abedy101](https://github.com/abedy101)

Need this customized for your company’s documents or workflows?  
→ Open an issue or reach out directly.

---
