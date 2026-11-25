
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Document Question Answering System",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 AI-Based Document Question Answering System")

st.write(
    "Ask questions and get answers from the information "
    "available in the uploaded document."
)

st.divider()

# Create Knowledge Base
def create_knowledge_base(filename):
    knowledge_base = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    knowledge_base[key.strip().lower()] = value.strip()

        return knowledge_base

    except FileNotFoundError:
        return None


# Predefined rules
rules = {
    "course": ["course", "subject"],
    "course code": ["course code", "code"],
    "department": ["department"],
    "duration": ["duration", "how long"],
    "programming language": ["programming language", "language"],
    "knowledge representation": ["knowledge representation"],
    "search technique": ["search technique", "search method"],
    "reasoning technique": ["reasoning technique", "reasoning method"]
}


# Answer generation
def answer_question(question, knowledge_base):
    question = question.lower().strip()

    for key, keywords in sorted(
        rules.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        for word in keywords:
            if word in question and key in knowledge_base:
                return "The " + key + " is " + knowledge_base[key] + "."

    for key, value in knowledge_base.items():
        if key in question and key not in rules:
            return "The " + key + " is " + value + "."

    return "Information not found in the document."


# Load Knowledge Base
knowledge_base = create_knowledge_base("sample_document.txt")

if knowledge_base is None:
    st.error("Document not found. Please check sample_document.txt.")
else:
    st.success("Knowledge Base created successfully!")

    st.subheader("Ask Your Question")

    question = st.text_input(
        "Enter your question:",
        placeholder="Example: What is the course name?"
    )

    if st.button("Get Answer"):
        if question.strip():
            answer = answer_question(question, knowledge_base)

            st.subheader("Answer")
            st.info(answer)
        else:
            st.warning("Please enter a question.")

    st.divider()

    st.subheader("Available Document Information")

    for key, value in knowledge_base.items():
        st.write(f"**{key.title()}:** {value}")
