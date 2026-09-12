# 🎙️ Biz Voice AI

> **AI-powered voice customer support for modern businesses**

Biz Voice AI is an intelligent customer-support assistant designed to help businesses handle routine customer questions quickly and naturally.

Customers can ask questions about a business, and Biz Voice AI uses AI to generate a clear response based only on the business information provided. The response can also be spoken aloud using browser-based text-to-speech.

---

## ✨ Features

* 🤖 **AI-powered customer support**
* 💬 Natural-language question answering
* 🏢 Business information management
* 🔊 Voice response using text-to-speech
* 🎨 Modern dark-themed Streamlit interface
* 🔐 Secure OpenAI API key handling with Streamlit Secrets
* ⚡ Fast and simple interaction
* 🌐 Deployable through Streamlit Cloud
* 🧩 FastAPI backend for API-based integration

---

## 🏗️ How It Works

```text
Customer asks a question
        ↓
Biz Voice AI receives the question
        ↓
OpenAI processes the request
        ↓
Business information is provided as context
        ↓
AI generates a helpful response
        ↓
Response is displayed to the customer
        ↓
Response is spoken aloud 🔊
```

The AI is instructed to use only the available business information and avoid inventing prices, services, timings, or other details.

---

## 🛠️ Tech Stack

### Frontend / Interface

* **Streamlit**
* HTML/CSS
* Browser Speech Synthesis

### Backend

* **Python**
* **FastAPI**
* Pydantic
* CORS Middleware

### AI

* **OpenAI API**
* OpenAI Responses API

### Configuration

* `python-dotenv`
* Streamlit Secrets

### Deployment

* **Streamlit Cloud**
* GitHub

---

## 📁 Project Structure

```text
Biz Voice AI/
│
├── .gitignore
├── .env
├── README.md
├── requirements.txt
├── app.py
│
├── backend/
│   ├── main.py
│   ├── business_data.py
│   └── __pycache__/
│
├── frontend/
│   ├── index.html
│   └── script.js
│
└── venv/
```

### Main Files

| File                       | Purpose                               |
| -------------------------- | ------------------------------------- |
| `app.py`                   | Streamlit application and deployed UI |
| `backend/main.py`          | FastAPI backend and AI API endpoint   |
| `backend/business_data.py` | Business information                  |
| `frontend/index.html`      | Original frontend interface           |
| `frontend/script.js`       | Browser voice interaction             |
| `requirements.txt`         | Python dependencies                   |
| `.env`                     | Local API configuration               |

> `.env` and `venv/` are excluded from GitHub for security and environment management.

---

## 🏢 Demo Business

The current demo uses:

**Aisha Beauty Studio**

### Business Hours

10 AM – 8 PM

### Services

* Hair Styling
* Makeup
* Facial
* Appointments

### Pricing

Contact us for pricing.

The business information can be customized for other businesses.

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ZUMERAISHA/BIZ-VOICE-AI.git
cd BIZ-VOICE-AI
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your OpenAI API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

Never commit your `.env` file to GitHub.

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open locally in your browser.

---

## 🌐 Deployment

Biz Voice AI can be deployed using **Streamlit Cloud**.

For deployment:

1. Push the project to GitHub.
2. Connect the repository to Streamlit Cloud.
3. Select `app.py` as the main application file.
4. Add the OpenAI API key under **Streamlit Secrets**.

Example:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

Do not upload the `.env` file or expose your API key publicly.

---

## 🔐 Security

API keys should never be hard-coded into the source code.

For local development:

```env
OPENAI_API_KEY=your_api_key_here
```

For Streamlit Cloud, use **Secrets** instead of committing credentials to the repository.

The project `.gitignore` excludes sensitive and environment-specific files such as:

```text
.env
venv/
__pycache__/
*.pyc
```

---

## 💡 Example Questions

Users can ask questions such as:

```text
What are your business hours?
```

```text
What services do you offer?
```

```text
Do you provide makeup services?
```

```text
What are your prices?
```

If the requested information is not available, Biz Voice AI is instructed to tell the customer to contact the business instead of making up an answer.

---

## 🎯 Use Cases

Biz Voice AI can be adapted for:

* 💇 Beauty salons
* 🍽️ Restaurants
* 🏨 Hotels
* 🏥 Clinics
* 🛍️ Retail stores
* 📅 Appointment-based businesses
* 🏢 Small businesses
* 📞 Customer support systems

---

## 🔮 Future Improvements

Possible future enhancements include:

* 🎤 Real-time speech-to-text input
* 📞 Phone-call integration
* 📅 Automatic appointment booking
* 🗄️ Database integration
* 👥 Multi-business support
* 🌍 Multi-language voice support
* 📊 Customer interaction analytics
* 🧠 More advanced business knowledge management

---

## 👩‍💻 Project

**Biz Voice AI**
AI-powered voice customer support for businesses.

Built with Python, Streamlit, FastAPI, and OpenAI.

---

## 📜 License

This project is created for educational, demonstration, and hackathon purposes.
