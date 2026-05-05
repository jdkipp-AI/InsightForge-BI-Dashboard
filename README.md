```md
# InsightForge BI Dashboard

InsightForge is an AI-powered business intelligence dashboard that combines traditional data visualization with a Retrieval-Augmented Generation (RAG) assistant. The project is designed to help users explore business performance data through both charts and natural language interaction.

## Overview

This project demonstrates how AI can enhance business intelligence workflows by allowing users to ask questions about data in plain language. In addition to visualizing trends through a dashboard, InsightForge uses a RAG-based assistant to identify patterns, summarize findings, and support deeper exploration of business metrics.

For example, the system can help surface insights such as possible relationships between sales performance and customer satisfaction that may not be obvious from static charts alone.

## Key Features

- **AI Assistant:** Ask questions about the business data using a LangChain-powered assistant connected to OpenAI models.
- **Interactive Dashboard:** Explore performance trends through Streamlit-based visualizations.
- **RAG Workflow:** Uses retrieved business context to support more grounded AI responses.
- **Business Insight Focus:** Combines analytics and natural language interaction in a practical BI use case.

## Dashboard Preview

![Dashboard View](InsightForce%20Chart.png)  
*Sales and customer satisfaction visualization.*

## AI Interaction

![AI Chatbot](InsightForce%20Chatbot.png)  
*Example of the AI assistant identifying a quality gap between products.*

## Tech Stack

- **Language:** Python
- **Frameworks / Libraries:** LangChain, Streamlit, Pandas, Matplotlib, Seaborn
- **LLM Integration:** OpenAI API
- **Environment Management:** Conda

## How It Works

1. Business data is loaded and prepared for analysis.
2. The dashboard displays key metrics and visualizations in Streamlit.
3. Relevant business context is organized for retrieval.
4. A LangChain-based assistant uses retrieved context plus an OpenAI model to answer user questions.
5. Users can explore both visual and conversational insights in one interface.

## What I Built

In this project, I:
- Developed an interactive BI dashboard in Streamlit
- Integrated an AI assistant using LangChain and OpenAI APIs
- Structured business data for question-answering workflows
- Combined visualization and conversational AI into a single user experience
- Explored how RAG can improve business data interpretation

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/jdkipp-AI/InsightForge-BI-Dashboard.git
   cd InsightForge-BI-Dashboard
Install dependencies

bash
pip install -r requirements.txt
Set your OpenAI API key
PowerShell:

powershell
$env:OPENAI_API_KEY="your_key_here"
Launch the app

bash
streamlit run dashboard.py
Future Improvements
Add support for additional datasets
Improve prompt handling and response grounding
Expand dashboard filtering and interactivity
Strengthen evaluation of AI-generated insights
Purpose
This project was created as part of my applied AI portfolio and reflects my interest in combining business intelligence, data analysis, and LLM-powered tools in practical workflows.
