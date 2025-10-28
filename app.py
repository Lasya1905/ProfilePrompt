import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


with open("resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()


model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Streamlit App
st.title("Chatbot Portfolio")
st.subheader("Hi, I am Lasya's AI Assistant. How can I help you today?")

# Initialize chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box
user_input = st.chat_input("Type your question here... (e.g., internships, projects, skills)")


# Handle new input
if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Combine resume and question into one prompt
    prompt = f"""
        You are Lasya’s portfolio chatbot. Respond in a warm, approachable, and slightly enthusiastic tone, just like Lasya would. Use simple, clear language but also show curiosity and excitement when talking about technology, cybersecurity, or achievements.
        Your job is to answer any questions about *me* based on my resume below.
        - Always answer in third person using “Lasya” or “she”.
        - Use Relevant emojis while responding
        - When talking about my projects, highlight the problem-solving mindset behind them.
        - If the user asks about my technical skills, list them clearly and link them to my projects.
        - If the user asks for career goals, explain my passion for cybersecurity and continuous learning.
        - Try to end some answers with a light follow-up question to keep the conversation going.


        Here is my resume: 
        {resume_text}

        User's question: {user_input}
    """

    # Generate response from Gemini model
    response = model.generate_content(prompt)


    # Show response
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Add assistant's response to session state
    st.session_state.messages.append({"role": "assistant", "content": response.text})

# Suggested Questions Section
st.markdown("🤖 Suggested Questions")
suggested_questions = [
    "What are Lasya's key technical skills?",
    "Tell me about Lasya's cybersecurity experience.",
    "What internships has Lasya done?",
    "List projects mentioned in the resume.",
    "Summarize her educational background."
]

for question in suggested_questions:
    if st.button(question):
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": question})
        with st.chat_message("user"):
            st.markdown(question)

        # Use the same detailed prompt as regular input
        prompt = f"""
        You are Lasya's portfolio chatbot. Respond in a warm, approachable, and slightly enthusiastic tone, just like Lasya would. Use simple, clear language but also show curiosity and excitement when talking about technology, cybersecurity, or achievements.
        Your job is to answer any questions about *me* based on my resume below.
        - Always answer in third person using "Lasya" or "she".
        - Use Relevant emojis while responding
        - When talking about my projects, highlight the problem-solving mindset behind them.
        - If the user asks about my technical skills, list them clearly and link them to my projects.
        - If the user asks for career goals, explain my passion for cybersecurity and continuous learning.
        - Try to end some answers with a light follow-up question to keep the conversation going.


        Here is my resume: 
        {resume_text}

        User's question: {question}
        """
        
        # Generate response from Gemini model
        response = model.generate_content(prompt)
        
        # Show response
        with st.chat_message("assistant"):
            st.markdown(response.text)

        # Add assistant's response to session state
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        
        # Stop further processing after button click
        st.rerun()


# Sidebar
st.sidebar.title("Lasya Rao")
st.sidebar.image("image.png")
st.sidebar.markdown("Currently Interning as a Cybersecurity Intern at Women Safety Wing, Telangana Police")
st.sidebar.markdown("🎓 B.Tech CSE | IARE Hyderabad")
st.sidebar.markdown("🌐 [GitHub](https://github.com/Lasya1905)")
st.sidebar.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/lasya-rao-894282291/)")
st.sidebar.markdown("📫 [Email](mailto:klasyarao@gmail.com)")
with open("cyberresume.pdf","rb") as file:

    st.sidebar.download_button("Download Resume", file, "Resume_Cyber.pdf")







