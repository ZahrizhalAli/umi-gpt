import streamlit as st

st.set_page_config(page_icon="💬", page_title="UMI | AI Report", initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)
with st.container():

    st.markdown(
        f"""
    <div class="container">
        <header>AI Report | Universitas Muslim Indonesia</header>
        <a id="ai-report-btn" href="{st.secrets['BASE_URL']}/AI-Report" class="button-link">AI Report UMI [BETA]</a>
        <a id="ai-report-btn" href="https://chat.openai.com/g/g-NHnJaI0mv-ai-report" class="button-link">GPT 4+</a>
     
    </div>
        
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
         <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
    .button-link {
            width: 100%;
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        text-align: center;
        text-decoration: none;
        background-color: #4CAF50;
        color: #fff;
        border: none;
        cursor: pointer;
            margin: 5px;
        
    }
        .container {
            text-align: center;
        }

        header {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        button {
            width: 100%;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            box-sizing: border-box;
        }

        #ai-report-btn {
            background-color: #4CAF50;
            color: #fff;
            border: none;
        }

        #openai-btn {
            background-color: #008CBA;
            color: #fff;
            border: none;
        }
    </style>

          """,
        unsafe_allow_html=True,
    )
