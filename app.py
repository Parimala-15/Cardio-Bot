import streamlit as st
from chatbot import get_response
import random

# Set up page configuration
st.set_page_config(
    page_title="Cardio-Bot",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Heart Health Quotes
quotes = [
    "\"The greatest wealth is health.\" — Virgil",
    "\"Take care to get all the hearts you can, but don’t break any.\" — Unknown",
    "\"A healthy heart is a happy heart.\" — Unknown",
    "\"To keep the body in good health is a duty, otherwise we shall not be able to keep our mind strong and clear.\" — Buddha",
    "\"Heart health is the foundation of overall wellness.\" — Unknown",
    "\"Your heart is your most important organ. Don’t take it for granted.\" — Unknown",
    "\"Prevention is better than cure.\" — Desiderius Erasmus"
]

# Supportive and Hopeful Words
supportive_words = [
    "Keep going, your heart deserves the best care!",
    "Believe in yourself, your health journey matters.",
    "Every small step towards health is a big victory.",
    "A healthy heart is a happy heart—take care of it!",
    "Your heart is strong, and so are you!"
]

# Title Section with Hopeful Words
quote = random.choice(quotes)  # Random quote
supportive_message = random.choice(supportive_words)  # Random supportive message
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to right, #FF6F61, #FF4B4B, #FF7F50);
            font-family: 'Arial', sans-serif;
            margin: 0;
        }
        .main-title {
            font-size: 60px;
            font-weight: 900;
            color: #FFFFFF;
            text-align: center;
            margin-top: 80px;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.5);
        }
        .subtitle {
            font-size: 22px;
            color: #FFFFFF;
            text-align: center;
            font-weight: 600;
            margin-bottom: 30px;
        }
        .quote {
            font-size: 28px;
            color: #fff;
            font-style: italic;
            text-align: center;
            margin-bottom: 50px;
            font-weight: bold;
            background: linear-gradient(135deg, #FF4B4B, #FF6F61);
            border: 2px solid #FF6F61;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        .quote:hover {
            background: linear-gradient(135deg, #FF7F50, #FF4B4B);
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
            cursor: pointer;
            transform: scale(1.05);
        }
        .supportive-message {
            font-size: 22px;
            color: #FFFFFF;
            text-align: center;
            font-weight: 500;
            margin-bottom: 40px;
            background-color: rgba(0, 0, 0, 0.4);
            border-radius: 8px;
            padding: 15px;
        }
        .chatbox-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 50px;
        }
        .chat-header {
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 25px;
            font-weight: 700;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        .chat-input {
            width: 80%;
            padding: 18px;
            font-size: 18px;
            border-radius: 12px;
            border: 2px solid #FF4B4B;
            background-color: rgba(255, 255, 255, 0.8);
            margin-bottom: 20px;
            outline: none;
            transition: 0.3s ease;
        }
        .chat-input:focus {
            border-color: #FF6F61;
            background-color: rgba(255, 255, 255, 1);
            box-shadow: 0 0 10px rgba(255, 105, 180, 0.7);
        }
        .response {
            font-size: 20px;
            color: white;
            margin-top: 30px;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 10px;
            width: 80%;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
        }
    </style>
    <div class="main-title">Cardio-Bot</div>
    <div class="subtitle">Your heart health companion</div>
    <div class="quote">""" + quote + """</div>
    <div class="supportive-message">""" + supportive_message + """</div>
    """,
    unsafe_allow_html=True
)

# Image Section
st.image(
    "healthy-heart.jpg",
    caption="Stay heart-healthy with Cardio-Bot!",
    use_container_width=True
)

# Chatbot UI Section
st.markdown('<div class="chatbox-container">', unsafe_allow_html=True)
st.markdown('<div class="chat-header">Chat with Cardio-Bot</div>', unsafe_allow_html=True)

# User input and response
user_input = st.text_input("Ask me anything about heart health:", key="user_input", placeholder="Type your question here...", label_visibility="collapsed", max_chars=300)

if user_input:
    response = get_response(user_input)
    st.markdown(f'<div class="response">{response}</div>', unsafe_allow_html=True)

    # After response, show a thank you message
    st.markdown(
        """
        <div style="font-size: 24px; color: #FF6F61; text-align: center; margin-top: 30px; font-weight: bold;">
            Thank you for reaching out! Stay heart-healthy and keep smiling! 😊
        </div>
        """,
        unsafe_allow_html=True
    )






#cd C:\Users\parim\Documents
# python -m streamlit run app.py




