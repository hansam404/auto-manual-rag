🚗 AutoMechanic RAG: Production-Ready AI Assistant

A fully containerized, production-grade Retrieval-Augmented Generation (RAG) application. This project ingests heavy automotive service manuals (PDFs) and provides an interactive chatbot interface to answer highly technical mechanic questions with zero hallucinations.

The goal of this repository is to demonstrate Cloud-Native AI Engineering best practices, including automated CI/CD pipelines, strict code linting, unit testing with mocks, and modular ETL architecture.

🧠 System Architecture

This application follows a strict Extract, Transform, Load (ETL) and Retrieval workflow:

[User Input] ──> (Streamlit UI) ──> [Query]
                                      │
                                      ▼
[PDF Manual] ──> (Chunking) ──> [Vector DB] ──(Retrieval)──> [Context]
                                                               │
                                                               ▼
                                                        [LLM (Gemini)] ──> [Response]


🛠️ Tech Stack & Engineering Practices

The AI & Data Stack

Orchestration: LangChain

LLM Engine: Google Gemini (gemini-1.5-flash)

Vector Embeddings: Hugging Face (all-MiniLM-L6-v2 - run entirely locally to save API costs)

Vector Database: ChromaDB (Local persistent storage)

Frontend: Streamlit

The Production/DevOps Stack

CI/CD Automation: GitHub Actions (Automated testing and linting on every push/PR).

Unit Testing: Pytest (Utilizing unittest.mock.patch to test chunking logic without requiring heavy PDF uploads to the cloud).

Linting & Formatting: Ruff (Enforcing strict PEP-8 standards at blazing fast speeds).

Environment Management: Python venv and python-dotenv for secure secret handling.

🚀 Getting Started (Local Development)

1. Clone & Environment Setup

Ensure you have Python 3.10+ installed. Professionals use isolated virtual environments:

git clone [https://github.com/your-username/auto-manual-rag.git](https://github.com/your-username/auto-manual-rag.git)
cd auto-manual-rag

# Create and activate the sandbox
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies cleanly
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt


2. Configure API Keys

Create a .env file in the root directory and add your free Google AI Studio key:

GOOGLE_API_KEY=your_gemini_api_key_here


3. Run the ETL Pipeline (Build Database)

Place your target PDF manual inside the data/ folder (e.g., data/manual.pdf), then run the ingestion script to build the local vector database:

python -m src.database


4. Launch the App

Fire up the Streamlit UI to interact with your manual:

streamlit run app.py


🧪 Testing & Quality Assurance

This project enforces strict code quality. To run the test suite locally:

# Run unit tests
python -m pytest tests/

# Run the linter and auto-formatter
ruff check .
ruff format .
