# Agentic AI Projects

A collection of AI-powered applications built with Python, Agno, and Large Language Models (LLMs). This repository explores multi-agent systems, persistent memory, financial research, and YouTube video analysis.

## Projects

### 1. Multilingual AI Team
- Uses multiple agents to answer questions in English, Hindi, and Chinese.
- Demonstrates agent coordination and role-based instructions.

### 2. AI Financial Research Agent
- Explores stock research and financial information retrieval.
- Integrates financial tools and language models.

### 3. AI Agent Memory
- Demonstrates user-specific memory and conversation history.
- Uses SQLite for persistent storage.

### 4. YouTube Video Analyzer
- Analyzes YouTube videos using available transcript and metadata tools.
- Produces summaries, topic breakdowns, and timestamped insights.

### 5. Streamlit Web Interface
- Provides a web interface for interacting with AI-powered features.

## Tech Stack

- Python
- Agno
- OpenAI API and other supported LLM providers
- Streamlit
- SQLite
- YouTube Transcript API
- YFinance
- DuckDuckGo Search

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hamza5212/Agentic-ai.git
cd Agentic-ai
```

### 2. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file and add the API keys required by your selected projects.

```env
OPENAI_API_KEY=your_openai_api_key
gemini_api=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Only configure the keys required by the application you intend to run. Never commit `.env` or expose API keys publicly.

### 4. Run the Streamlit app

```bash
streamlit run ui.py
```

## Deployment

The Streamlit application can be deployed using Streamlit Community Cloud by connecting the GitHub repository, selecting `ui.py` as the main file, and configuring secrets securely.

## Notes

- API access and usage limits depend on the selected provider and account.
- Some features require valid API credentials and external service availability.
- This repository is an evolving learning project exploring practical Agentic AI workflows.

## Author

Hamza Selanawala
