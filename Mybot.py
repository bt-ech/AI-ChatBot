import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Validate the API key
if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Function to get a response from the OpenAI API
def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or use "gpt-4"
        messages=messages,
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].message["content"]

# Streamlit app layout
st.title("AI Chatbot")

st.write("Ask me anything!")

# User input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    # Add user input to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get the bot response
    bot_response = get_openai_response(st.session_state.messages)

    # Add the bot response to the session state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Display the conversation
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        elif message["role"] == "assistant":
            st.write(f"**Bot:** {message['content']}")
