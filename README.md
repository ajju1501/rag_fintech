# 📉 RAG Fintech Assistant – Real-Time Stock & Company Insights (India)

This is an AI-powered Retrieval-Augmented Generation (RAG) application that fetches **real-time stock data** from [Screener.in](https://www.screener.in) and uses **Gemini (Google's LLM)** to provide natural language responses to financial queries like:

> "What is the PE ratio of Reliance?"
> "Tell me the ROE and Debt to Equity of TCS."
> "What are the key financial ratios of Infosys?"

---

## 🚀 Features

* 🔎 **Real-time financial data** for all Indian listed companies
* 🤖 **Gemini 2.5 Flash** LLM for intelligent answers
* 🧠 Uses RAG pattern: retrieval + generation
* 💻 Built with **Python + Streamlit**
* 🔐 API key secured via `.env`
* 🧪 Easily extendable for news, filings, sentiment, etc.

---

## 💻 Tech Stack

| Layer          | Tech                                |
| -------------- | ----------------------------------- |
| Language Model | Gemini 2.5 Flash (Google AI)        |
| Frontend       | Streamlit                           |
| Scraping      | `requests` + `BeautifulSoup`        |
| Env Config     | `dotenv`                           |
| Hosting        | GitHub + Streamlit Cloud (optional) |

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/RamGrandhi71/rag-fintech-app.git
cd rag-fintech-app

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Setup Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

Do **not** commit `.env` (already ignored via `.gitignore`).

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the link shown in the terminal (usually `http://localhost:8501`).

---

## ✍️ Example Queries

```txt
What is the PE ratio of RELIANCE?
Tell me the debt to equity and return on equity of INFY.
What are key financials of SBIN?
```

---

## ✅ To Do (Next Steps)

* [ ] Add news scraping and RAG for latest headlines
* [ ] Add visual graphs (e.g. stock trends)
* [ ] Connect with NSE/BSE APIs for intraday prices
* [ ] Deploy on Streamlit Cloud

---

## 🤝 Contributing

Pull requests are welcome! Open an issue for suggestions, bugs, or new ideas.

---

## 📄 License

MIT License — feel free to fork and build upon.

---

## 🙌 Acknowledgements

* [Screener.in](https://www.screener.in) — Real-time company data
* [Gemini](https://ai.google.dev) — Google's LLM
* [Streamlit](https://streamlit.io) — Fast UI for ML apps
