from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import random

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Generative AI model
model = genai.GenerativeModel("gemini-pro")

def generate_questions(topic, subtopic):
    """Generate 20 unique questions (theoretical and practical) for a given subtopic."""
    unique_identifier = random.randint(1, 1000000)  # Ensure new questions are generated each time
    query = (
        f"Generate 20 interview preparation questions (theoretical and practical) for the subtopic '{subtopic}' "
        f"under the topic '{topic}' related to the MERN stack. Add a unique identifier {unique_identifier} to ensure freshness."
    )
    response = model.generate_content(query)
    return response.text

# Streamlit UI setup
st.set_page_config(page_title="MERN Trainer Chatbot", layout="wide")
st.title("MERN Trainer Chatbot")
st.markdown(
    "Prepare for your MERN stack interviews with tailored questions for each topic and subtopic!"
)

# Dropdown for main topics
topics = ["MongoDB", "React", "Express.js", "Node.js"]
selected_topic = st.selectbox("Select a topic:", ["Select"] + topics)

# Subtopics for each main topic
subtopics = {
    "MongoDB": ["Basics", "CRUD Operations", "Indexing", "Aggregation", "Replication", "Sharding"],
    "React": ["Components", "State Management", "Hooks", "Lifecycle Methods", "Routing", "Performance Optimization"],
    "Express.js": ["Middleware", "Routing", "Error Handling", "Authentication", "REST APIs", "Template Engines"],
    "Node.js": ["Event Loop", "Streams", "File System", "Modules", "Error Handling", "Performance Optimization"],
}

if selected_topic != "Select":
    selected_subtopic = st.selectbox(
        f"Select a subtopic under {selected_topic}:", ["Select"] + subtopics[selected_topic]
    )

    if selected_subtopic != "Select":
        if st.button(f"Generate Questions for {selected_subtopic}"):
            st.subheader(f"{selected_topic} - {selected_subtopic} Interview Preparation Questions")
            st.write("Generating fresh questions... Please wait.")
            questions = generate_questions(selected_topic, selected_subtopic)
            st.write(questions)

st.write("\n")
st.info("Select a topic and subtopic to generate interview preparation questions. Fresh questions are guaranteed every time.")
