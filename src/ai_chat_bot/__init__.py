import streamlit as st
import st_tailwind as tw
from ai_chat_bot.chat_bot import chat_bot 

def main():
    if "prompt" not in st.session_state:
        st.session_state.prompt = ""

    if "response" not in st.session_state:
        st.session_state.response = ""


    st.html(f"""<h1 style='font-size: 30px; color: black; margin-top: 2px;'>Chatbot App By <a href="https://www.linkedin.com/in/abdullah-shaikh-29699b302/" target="_blank" style="color:blue";>Abdullah Shaikh</a></h1>
    """)
    st.write(st.session_state.response)
    st.session_state.prompt = tw.text_input(label="", placeholder="Enter Your Prompt",classes="mt-[370px]")

    if st.button("Respond",key=1):
        st.session_state.response = chat_bot(st.session_state.prompt)
        tw.write("Your Response is ready click on belw button to see!",classes="text-red-400")

    if st.button("Show Response",key=2):
        pass

if __name__ == "__main__":
    main()