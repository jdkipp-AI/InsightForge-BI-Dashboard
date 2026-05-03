import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 2. Load our "Knowledge Base" context
with open('data_context.txt', 'r') as f:
    context = f.read()

# 3. Design the Prompt
template = """
You are InsightForge, an expert Business Intelligence Assistant. 
Use the following data summary to answer the user's question.

Business Data Summary:
{context}

User Question: {question}

Answer:"""

prompt = PromptTemplate.from_template(template)

# 4. Set up the Chain (Modern LCEL Style: Prompt -> LLM -> Output Parser)
chain = prompt | llm | StrOutputParser()

# 5. Ask a test question
question = "Our average satisfaction is 3.03. Which product has the highest satisfaction, and does our top-selling product (Widget A) also have the highest satisfaction?"
response = chain.invoke({"context": context, "question": question})

print("\n--- AI Assistant Response ---")
print(response)