import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy")
st.write("Ask any study-related question!")

# Read API key from Streamlit Secrets
client = genai.Client(api_key="AQ.Ab8RN6L2eTe1Db-3oMeS8XHzCP162JbcE7BWmlpYiRVuXbPhOg")

question = st.text_input("Enter your question")

if st.button("Ask AI"):
    if question.strip():
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )
            st.success(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
