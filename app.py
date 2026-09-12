import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import urllib.parse


# =========================================================
# API SETUP
# =========================================================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("OPENAI_API_KEY")

# Streamlit Cloud Secrets
if not api_key:
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("OPENAI_API_KEY .env file ya Streamlit Secrets mein nahi mili.")
    st.stop()

client = OpenAI(api_key=api_key)


# =========================================================
# BUSINESS INFORMATION
# =========================================================

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


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Biz Voice AI",
    page_icon="🎙️",
    layout="centered"
)


# =========================================================
# DARK ELEGANT DESIGN
# =========================================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */

    .stApp {
        background: linear-gradient(
            135deg,
            #0b0b0b 0%,
            #151515 50%,
            #0d0d0d 100%
        );

        color: #f5f1eb;
    }


    /* MAIN CONTAINER */

    .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* HIDE STREAMLIT DEFAULT ELEMENTS */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* HERO */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #f5f1eb;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #b9afa4;
    }

    .gold-line {
        width: 70px;
        height: 3px;
        background: #c49a63;
        margin: 18px auto 25px auto;
        border-radius: 10px;
    }


    /* BUSINESS CARD */

    .business-card {
        background: #191919;
        border: 1px solid #302c28;
        border-radius: 20px;
        padding: 25px;
        margin-top: 15px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }

    .business-name {
        font-size: 25px;
        font-weight: 700;
        color: #f5f1eb;
        margin-bottom: 15px;
    }

    .info-text {
        color: #c3bbb2;
        font-size: 15px;
        margin: 9px 0;
    }

    .info-text b {
        color: #e0b77f;
    }


    /* RESPONSE CARD */

    .response-card {
        background: #1b1b1b;
        color: #f5f1eb;
        border: 1px solid #332d27;
        border-radius: 20px;
        padding: 25px;
        margin-top: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }

    .response-title {
        color: #d9b887;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 10px;
    }


    /* VOICE TEXT */

    .voice-text {
        text-align: center;
        color: #a99e93;
        font-size: 14px;
        margin-top: 12px;
    }


    /* BUTTON */

    .stButton > button {
        width: 100%;
        border-radius: 14px;
        border: 1px solid #4a3b2d;
        background: #c49a63;
        color: #111111;
        font-size: 16px;
        font-weight: 700;
        padding: 12px;
    }

    .stButton > button:hover {
        background: #dfb982;
        color: #111111;
        border-color: #dfb982;
    }


    /* TEXT INPUT */

    .stTextInput input {
        border-radius: 14px;
        border: 1px solid #403a35;
        background: #191919;
        color: #f5f1eb;
        padding: 14px;
    }

    .stTextInput input::placeholder {
        color: #8e857c;
    }

    .stTextInput input:focus {
        border-color: #c49a63;
        box-shadow: 0 0 0 1px #c49a63;
    }


    /* STREAMLIT HEADINGS */

    h1, h2, h3 {
        color: #f5f1eb !important;
    }


    /* INFO / WARNING */

    .stAlert {
        background: #1b1b1b;
        color: #f5f1eb;
        border-radius: 14px;
    }


    /* SPINNER TEXT */

    .stSpinner > div {
        color: #d9b887;
    }


    /* FOOTER */

    .footer-text {
        text-align: center;
        color: #77706a;
        font-size: 13px;
        margin-top: 35px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
    '<div class="main-title">🎙️ Biz Voice AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Intelligent voice support for modern businesses</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="gold-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask a question. Get an answer. Hear it instantly.</div>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# BUSINESS INFORMATION
# =========================================================

st.subheader("🏢 Business Information")

st.markdown(
    '<div class="business-card">',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="business-name">{business_info["name"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="info-text">🕐 <b>Hours:</b> {business_info["hours"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="info-text">✨ <b>Services:</b> {", ".join(business_info["services"])}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="info-text">💳 <b>Pricing:</b> {business_info["pricing"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# ASK AI
# =========================================================

st.subheader("💬 Ask Your Question")

question = st.text_input(
    "Ask anything about the business",
    placeholder="e.g. What are your business hours?",
    label_visibility="collapsed"
)

ask_button = st.button("Ask AI ✨")


# =========================================================
# AI RESPONSE
# =========================================================

if ask_button:

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        business_details = f"""
Business Name: {business_info["name"]}
Business Hours: {business_info["hours"]}
Services: {", ".join(business_info["services"])}
Pricing: {business_info["pricing"]}
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

        answer = response.output_text


        # =================================================
        # AI RESPONSE
        # =================================================

        st.markdown(
            '<div class="response-card">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="response-title">🤖 Biz Voice AI</div>',
            unsafe_allow_html=True
        )

        st.write(answer)

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="voice-text">🔊 AI response is being spoken aloud</div>',
            unsafe_allow_html=True
        )


        # =================================================
        # VOICE OUTPUT
        # =================================================

        speech_html = f"""
        <script>

        const text = {answer!r};

        if ("speechSynthesis" in window) {{

            window.speechSynthesis.cancel();

            const speech =
                new SpeechSynthesisUtterance(text);

            speech.lang = "en-US";
            speech.rate = 0.95;
            speech.pitch = 1;

            window.speechSynthesis.speak(speech);
        }}

        </script>
        """

        speech_url = (
            "data:text/html;charset=utf-8,"
            + urllib.parse.quote(speech_html)
        )

        st.iframe(
            speech_url,
            height=1
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer-text">Powered by AI • Biz Voice AI</div>',
    unsafe_allow_html=True
)
