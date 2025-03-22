# AI Chatbot using LangGraph, FastAPI, and Streamlit

This project demonstrates how to build a powerful AI chatbot using **LangGraph**, **FastAPI**, and **Streamlit**. The chatbot supports dynamic model selection, processes requests via a FastAPI backend, and offers an intuitive UI for user interaction.

## 🚀 Features
- **FastAPI Backend**: Handles chatbot requests efficiently.
- **LangGraph Agents**: Enables dynamic AI model selection.
- **Streamlit UI**: Provides an easy-to-use interface for users.
- **Scalable Architecture**: Designed for performance and expandability.

## 🛠️ Technologies Used
- Python
- LangGraph
- FastAPI
- Streamlit
- OpenAI API (or other LLM APIs)

## 📌 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/HamzaaAftab/Ai-Agent-Chatbot-using-Streamlit-Fastapi-Langgraph.git
cd Ai-Agent-Chatbot-using-Streamlit-Fastapi-Langgraph
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your API key:
```sh
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run the FastAPI Backend
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 6️⃣ Run the Streamlit Frontend
```sh
streamlit run app.py
```

## 📌 API Endpoints
| Method | Endpoint       | Description               |
|--------|---------------|---------------------------|
| POST   | `/chat`        | Processes user messages   |
| GET    | `/health`      | Checks server status      |

## 📌 Folder Structure
```
📂 Ai-Agent-Chatbot
├── 📂 backend (FastAPI Server)
├── 📂 frontend (Streamlit UI)
├── app.py (Main Streamlit App)
├── app.py (FastAPI App)
├── requirements.txt
├── .gitignore
└── README.md
```

## 💡 Future Improvements
- Add multi-model support.
- Implement a database for conversation history.
- Improve response accuracy with fine-tuned models.

## 📜 License
This project is licensed under the **MIT License**.

---

### 🔥 Developed by [Your Name] | [GitHub Profile] 🚀