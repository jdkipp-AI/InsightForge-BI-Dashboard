# InsightForge: AI-Powered BI Dashboard

An advanced Business Intelligence tool that combines traditional data visualization with a **Retrieval-Augmented Generation (RAG)** assistant.

## Project Overview
InsightForge allows users to interact with business data using natural language. It identifies trends—like the inverse correlation between sales volume and customer satisfaction—that traditional dashboards often miss.

### Key Features
*   **AI Assistant:** Chat directly with your data using OpenAI's GPT models via LangChain.
*   **Live Dashboard:** Real-time data visualization powered by Streamlit.
*   **Knowledge Base:** Automated data aggregation and context generation for LLMs.

## Dashboard Preview
![Dashboard View](InsightForge%20Chart.png)
*Visualizing Sales vs. Satisfaction performance.*

## AI Interaction
![AI Chatbot](InsightForge%20Chatbot.png)
*The RAG system identifying the "Widget A vs. Widget D" quality gap.*

## Tech Stack
*   **Environment:** Conda (Python 3.12)
*   **Logic:** LangChain, OpenAI API
*   **Data:** Pandas, Matplotlib, Seaborn
*   **UI:** Streamlit

## How to Run
1.  **Clone the repo:** `git clone https://github.com`
2.  **Install dependencies:** `pip install -r requirements.txt`
3.  **Set your API Key:** `$env:OPENAI_API_KEY = "your_key_here"`
4.  **Launch:** `streamlit run dashboard.py`
