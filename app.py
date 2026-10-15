import streamlit as st
import requests

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="centered"
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

st.title("📚 StudyMate AI")
st.subheader("Your Personal AI Study Assistant")
st.write("Turn your study notes into useful learning resources with local AI.")

study_text = st.text_area(
    "Paste your study notes here:",
    placeholder="Paste your lecture notes or learning materials...",
    height=220
)

mode = st.radio(
    "Choose a learning tool:",
    ["Summary", "Key Points", "Practice Questions"]
)

def ask_ai(notes, task):
    prompts = {
        "Summary": (
            "Summarize the following study notes in clear Chinese. "
            "Organize the main ideas and preserve important facts."
        ),
        "Key Points": (
            "Extract 3 to 5 important key points from the following notes. "
            "Explain each point clearly in Chinese."
        ),
        "Practice Questions": (
            "Create 5 practice questions in Chinese based on the notes. "
            "Include answers and brief explanations."
        )
    }

    prompt = (
        f"{prompts[task]}\n\n"
        f"Study notes:\n{notes}\n\n"
        "Only use information supported by the notes. "
        "If information is insufficient, say so."
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    return response.json()["response"]

if st.button("Generate", type="primary"):
    if not study_text.strip():
        st.warning("Please enter some study notes first.")
    else:
        try:
            with st.spinner("AI is processing your notes..."):
                result = ask_ai(study_text, mode)

            st.subheader(mode)
            st.markdown(result)

        except requests.exceptions.ConnectionError:
            st.error(
                "Cannot connect to Ollama. Please make sure Ollama "
                "is running on your Mac."
            )
        except requests.exceptions.Timeout:
            st.error(
                "The model took too long to respond. Please try shorter notes."
            )
        except requests.exceptions.RequestException as e:
            st.error(f"AI request failed: {e}")
        except (KeyError, ValueError):
            st.error("The model returned an unexpected response.")