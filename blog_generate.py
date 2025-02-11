import streamlit as st
import google.generativeai as genai

# Set Streamlit page config
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize Google Gemini API (Replace with your actual API key)
GENAI_API_KEY = "AIzaSyChpvT-miHvwDxWxxkjgHJCGk4OL8Dcv5w"
genai.configure(api_key=GENAI_API_KEY)

# Function to generate blog using Google Gemini AI
def generate_blog(topic, no_words, blog_style):
    prompt = f"You are a professional blog writer. Write a {no_words}-word blog on '{topic}' for {blog_style}."
    
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use latest available Gemini model
    response = model.generate_content(prompt)

    # Check if response contains text
    return response.text if hasattr(response, "text") else "Error generating blog. Try again."

# Streamlit UI
st.header("AI Blog Generator 🤖")

# User inputs
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words', value="150")
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

# Generate and display the blog
if submit:
    if input_text and no_words.isdigit():
        with st.spinner("Generating blog... Please wait ⏳"):
            blog_content = generate_blog(input_text, no_words, blog_style)
        st.subheader("Generated Blog:")
        st.write(blog_content)
    else:
        st.warning("Please enter a valid blog topic and number of words (numeric).")

