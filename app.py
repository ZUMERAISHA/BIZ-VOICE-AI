import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os


# Project folder
BASE_DIR = Path(__file__).resolve().parent

# .env load karo
load_dotenv(BASE_DIR / ".env")

# API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OPENAI_API_KEY .env file mein nahi mili.")
    st.stop()

client = OpenAI(api_key=api_key)


# Business information
business_info = {
    "name": "Aisha Beauty Studio",
    "hours": "10 AM - 8 PM",
    "services": [
        "Hair Styling",
        "Makeup",
        "Facial",
        "Appointments"
    ],
    "pricing": "Contact us for pricing"
}


# Page settings
st.set_page_config(
    page_title="Biz Voice AI",
    page_icon="🎙️"
)

st.title("🎙️ Biz Voice AI")
st.write("AI-powered customer support assistant for businesses.")

st.divider()

# Business information
st.subheader("🏢 Business Information")

st.write(f"**Business:** {business_info['name']}")
st.write(f"**Hours:** {business_info['hours']}")
st.write(f"**Services:** {', '.join(business_info['services'])}")
st.write(f"**Pricing:** {business_info['pricing']}")

st.divider()

# Customer question
st.subheader("💬 Ask a Question")

question = st.text_input(
    "What would you like to know?"
)

if st.button("Ask AI 🤖"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        business_details = f"""
Business Name: {business_info['name']}
Business Hours: {business_info['hours']}
Services: {', '.join(business_info['services'])}
Pricing: {business_info['pricing']}
"""

        with st.spinner("AI is thinking..."):

            response = client.responses.create(
                model="gpt-5.6-luna",
                instructions=(
                    "You are Biz Voice AI, a helpful business customer support assistant. "
                    "Answer clearly, naturally, and briefly. "
                    "Only use the business information provided below. "
                    "Do not invent services, prices, timings, or other business details. "
                    "If the information is not available, politely tell the customer "
                    "to contact the business.\n\n"
                    "BUSINESS INFORMATION:\n"
                    + business_details
                ),
                input=question
            )

        st.subheader("🤖 AI Response")
        st.success(response.output_text)