StudyMate AI 📚
A lightweight AI-powered study assistant built with Python, Streamlit, and Ollama.

Features
Study Summaries — Generate concise summaries from study notes.
Key Points — Extract important concepts from learning materials.
Practice Questions — Generate review questions with answers and explanations.
Local AI Inference — Run the language model locally through Ollama without requiring a cloud API key.
Tech Stack
Python
Streamlit
Ollama
Llama 3.2
Prerequisites
Python 3
Ollama
The llama3.2 model
Getting Started
1. Clone the repository
git clone YOUR_GITHUB_REPOSITORY_URL
cd StudyMateAI
2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
4. Download the model
ollama pull llama3.2
Make sure Ollama is running before launching the app.

5. Run the application
python -m streamlit run app.py
Open http://localhost:8501 in your browser.

Project Status
A beginner-friendly portfolio project demonstrating local LLM integration and AI-assisted learning workflows.

Future Improvements
Support uploading study materials
Add downloadable study notes
Improve question generation and answer evaluation
Add a more polished user interface
License
MIT