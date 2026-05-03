import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Page Config
st.set_page_config(page_title="InsightForge BI Dashboard", layout="wide")

st.title("🚀 InsightForge: Business Intelligence Dashboard")

# Load Data
df = pd.read_csv('sales_data.csv')

# --- Sidebar Summary ---
st.sidebar.header("Key Metrics")
st.sidebar.metric("Total Sales", f"${df['Sales'].sum():,.2f}")
st.sidebar.metric("Avg Satisfaction", f"{df['Customer_Satisfaction'].mean():.2f}/5")

# --- Layout: Charts ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Product")
    product_sales = df.groupby('Product')['Sales'].sum().reset_index()
    # Using Matplotlib for Sales to control the Y-axis range
    fig1, ax1 = plt.subplots()
    sns.barplot(data=product_sales, x='Product', y='Sales', ax=ax1, palette="Blues_r")
    
    # Adjust range: Start at 300k to show the drop-off from Widget A
    ax1.set_ylim(300000, 400000) 
    st.pyplot(fig1)

with col2:
    st.subheader("Customer Satisfaction by Product")
    sat_data = df.groupby('Product')['Customer_Satisfaction'].mean().reset_index()
    fig2, ax2 = plt.subplots()
    sns.barplot(data=sat_data, x='Product', y='Customer_Satisfaction', ax=ax2, palette="viridis")
    
    # Adjust range: Start at 2.8 to show Widget D's lead clearly
    ax2.set_ylim(2.8, 3.2) 
    ax2.set_ylabel("Avg Satisfaction Score")
    st.pyplot(fig2)

# --- Raw Data Toggle ---
if st.checkbox("Show Raw Data"):
    st.write(df)
    
# Reuse the context we built earlier
with open('data_context.txt', 'r') as f:
    context = f.read()

user_input = st.text_input("Ask a question about your business data:")

if user_input:
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import PromptTemplate
    from langchain_core.output_parsers import StrOutputParser

    # Initialize AI
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    template = "You are a BI assistant. Use this data: {context}. Question: {question}"
    prompt = PromptTemplate.from_template(template)
    
    # Modern Chain
    chain = prompt | llm | StrOutputParser()
    
    with st.spinner("Thinking..."):
        response = chain.invoke({"context": context, "question": user_input})
        st.write("### AI Response:")
        st.info(response)