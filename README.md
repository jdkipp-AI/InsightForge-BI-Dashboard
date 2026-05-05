# InsightForge BI Dashboard

InsightForge BI Dashboard is an AI-powered business intelligence application that combines
interactive data visualization with conversational analytics. Built with Streamlit, LangChain,
and OpenAI, the project demonstrates how users can explore business data through both traditional
dashboard views and natural-language questions.

---

## Project Summary

This project showcases how generative AI can enhance business intelligence workflows by making
data more accessible, interactive, and actionable. In addition to visualizing performance metrics,
InsightForge enables users to ask questions about the data and receive context-aware responses
supported by retrieval-based processing.

The goal is to bridge the gap between static reporting and intelligent decision support by
creating a unified analytics experience.

---

## Features

- **Interactive BI Dashboard** — Visualize business performance metrics and trends through an
  intuitive Streamlit interface.
- **Conversational AI Assistant** — Ask natural-language questions about the dataset using a
  LangChain-powered assistant integrated with OpenAI.
- **Retrieval-Augmented Generation (RAG)** — Improves response relevance by supplying the model
  with retrieved business context before generating answers.
- **Business-Focused Insights** — Designed to highlight meaningful operational patterns, such as
  sales performance, customer satisfaction, and product quality relationships.
- **Unified Analytics Experience** — Combines structured dashboard exploration with AI-driven
  question answering in a single application.

---

## Dashboard Preview

> *Example dashboard view showing business performance and customer satisfaction trends.*

---

## AI Assistant Preview

> *Example of the AI assistant identifying a potential quality gap between products.*

---

## Tech Stack

|
 Category                  
|
 Technology                  
|
|
---------------------------
|
-----------------------------
|
|
 Programming Language      
|
 Python                      
|
|
 Frontend / App Framework  
|
 Streamlit                   
|
|
 AI / LLM Framework        
|
 LangChain                   
|
|
 LLM Provider              
|
 OpenAI API                  
|
|
 Data Tools                
|
 Pandas, Matplotlib, Seaborn 
|
|
 Environment Management    
|
 Conda                       
|

---

## How It Works

1. Business data is loaded and prepared for analysis.
2. Key metrics and trends are displayed through interactive dashboard components.
3. Relevant business context is structured for retrieval.
4. User questions are routed through a LangChain workflow.
5. Retrieved context is passed to the OpenAI model to generate grounded responses.
6. Users gain insights through both visual analysis and conversational interaction.

---

## What I Built

In this project, I:

- Developed an interactive business intelligence dashboard using Streamlit
- Integrated a conversational AI assistant using LangChain and OpenAI
- Structured data to support retrieval-based question answering
- Created a practical portfolio project demonstrating applied AI in business intelligence

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jdkipp-AI/InsightForge-BI-Dashboard.git
cd InsightForge-BI-Dashboard
2. Install Dependencies
bash
pip install -r requirements.txt
3. Set Your OpenAI API Key
PowerShell:

powershell
$env:OPENAI_API_KEY="your_key_here"
Mac/Linux:

bash
export OPENAI_API_KEY="your_key_here"
4. Run the Application
bash
streamlit run dashboard.py
Future Enhancements
Add support for additional datasets and business domains
Improve prompt design and response grounding
Expand dashboard filters and interactive controls
Strengthen evaluation of AI-generated business insights
Improve scalability and modularity of the application architecture
Why This Project Matters
InsightForge reflects the growing role of generative AI in analytics and decision support.
This project was created as part of an applied AI portfolio and highlights an interest in
building practical, real-world AI solutions.
---
