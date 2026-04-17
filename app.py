import streamlit as st
from google import genai

# Page Config
st.set_page_config(page_title="Gemma 4 Post Creator", page_icon="🤖")

st.title("🤖 Gemma 4: LinkedIn Post Agent")
st.write("Turn your daily wins into professional LinkedIn content.")

# Sidebar for API Key (Better for security)
api_key = st.sidebar.text_input("Enter your API key", type="password")

if api_key:
    client = genai.Client(api_key=api_key)

    # Input Fields
    with st.form("post_form"):
        topic = st.text_input("What did you build/do today?", placeholder="e.g. Built a weather app with Python")
        struggle = st.text_area("What was the biggest challenge?", placeholder="e.g. Debugging the API response")
        lesson = st.text_input("What's the key takeaway?", placeholder="e.g. Documentation is your best friend")
        
        style = st.select_slider("Select Tone", options=["Casual", "Professional", "Hype/Viral"])
        
        submit = st.form_submit_button("Generate Post ✨")

    if submit:
        with st.spinner("Gemma 4 is thinking..."):
            prompt = f"""
            Role: Expert LinkedIn Content Creator.
            Input: 
            - Project: {topic}
            - Challenge: {struggle}
            - Lesson: {lesson}
            - Tone: {style}
            
            Task: Write a high-engagement LinkedIn post. Use a hook, line breaks for readability, 
            and mention you used 'Gemma 4' for the reasoning.
            """
            
            try:
                response = client.models.generate_content(model="gemma-4-31b-it", contents=prompt)
                st.success("Done!")
                st.subheader("Copy & Paste to LinkedIn:")
                st.write(response.text)
                st.button("Copy to Clipboard (Simulated)")
            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Please enter your API Key in the sidebar to start.")
