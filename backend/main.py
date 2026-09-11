from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
from .business_data import business_info
import os


# Project ka main folder
BASE_DIR = Path(__file__).resolve().parent.parent

# .env load karo
load_dotenv(BASE_DIR / ".env")

# API key read karo
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY .env file mein nahi mili.")

client = OpenAI(api_key=api_key)

app = FastAPI()


# Frontend ko backend se connect karne ki permission
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Biz Voice AI is working!"}


@app.get("/business")
def get_business_info():
    return business_info


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask_question(data: Question):

    business_details = f"""
Business Name: {business_info['name']}
Business Hours: {business_info['hours']}
Services: {', '.join(business_info['services'])}
Pricing: {business_info['pricing']}
"""

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
        input=data.question
    )

    return {
        "customer_question": data.question,
        "answer": response.output_text
    }