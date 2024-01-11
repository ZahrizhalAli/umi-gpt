import os
import streamlit as st
from io import StringIO
import re
import sys
from modules.history import ChatHistory
from modules.layout import Layout
from modules.utils import Utilities

#To be able to update the changes made to modules in localhost (press r)
def reload_module(module_name):
    import importlib
    import sys
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    return sys.modules[module_name]

history_module = reload_module('modules.history')
layout_module = reload_module('modules.layout')
utils_module = reload_module('modules.utils')

ChatHistory = history_module.ChatHistory
Layout = layout_module.Layout
Utilities = utils_module.Utilities

st.set_page_config(layout="wide", page_icon="💬", page_title="UMI | AI Report",initial_sidebar_state="collapsed" )

# Instantiate the main components
layout, utils = Layout(), Utilities()


st.markdown(
    f"""
    <h1 style='text-align: center;'> AI Report</h1>
    <h1 style='text-align: center;'> Universitas Muslim Indonesia Apps</h1>
    """,
    unsafe_allow_html=True,
)
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

user_api_key = utils.load_api_key()

if not user_api_key:
    layout.show_api_key_missing()
else:
    os.environ["OPENAI_API_KEY"] = user_api_key

    uploaded_file = utils.handle_upload(["pdf", "txt", "csv"])

    if uploaded_file:



        # Initialize chat history
        history = ChatHistory()
        try:
            chatbot = utils.setup_chatbot(
                uploaded_file, 'gpt-4-1106-preview', 0.2
            )
            st.session_state["chatbot"] = chatbot

            if st.session_state["ready"]:
                # Create containers for chat responses and user prompts
                response_container, prompt_container = st.container(), st.container()

                with prompt_container:
                    # Display the prompt form
                    is_ready, user_input = layout.prompt_form()

                    # Initialize the chat history
                    history.initialize(uploaded_file)

                    # Reset the chat history if button clicked
                    if st.session_state["reset_chat"]:
                        history.reset(uploaded_file)

                    if is_ready:
                        # Update the chat history and display the chat messages
                        history.append("user", user_input)

                        old_stdout = sys.stdout
                        sys.stdout = captured_output = StringIO()

                        output = st.session_state["chatbot"].conversational_chat(user_input)

                        sys.stdout = old_stdout

                        history.append("assistant", output)

                        # Clean up the agent's thoughts to remove unwanted characters
                        thoughts = captured_output.getvalue()
                        cleaned_thoughts = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', thoughts)
                        cleaned_thoughts = re.sub(r'\[1m>', '', cleaned_thoughts)

                        # Display the agent's thoughts
                        with st.expander("Display the agent's thoughts"):
                            st.write(cleaned_thoughts)

                history.generate_messages(response_container)
        except Exception as e:
            st.error(f"Error: {str(e)}")



# import streamlit as st
#
#
# #Config
# st.set_page_config(layout="wide", page_icon="💬", page_title="Robby | Chat-Bot 🤖")
#
#
# #Contact
# with st.sidebar.expander("📬 Contact"):
#
#     st.write("**GitHub:**",
# "[yvann-hub/Robby-chatbot](https://github.com/yvann-hub/Robby-chatbot)")
#
#     st.write("**Medium:** "
# "[@yvann-hub](https://medium.com/@yvann-hub)")
#
#     st.write("**Twitter:** [@yvann_hub](https://twitter.com/yvann_hub)")
#     st.write("**Mail** : barbot.yvann@gmail.com")
#     st.write("**Created by Yvann**")
#
# # 1_📄Robby-Chat
# #Title
# st.markdown(
#     """
#     <h2 style='text-align: center;'>Robby, your data-aware assistant 🤖</h1>
#     """,
#     unsafe_allow_html=True,)
#
# st.markdown("---")
#
#
# #Description
# st.markdown(
#     """
#     <h5 style='text-align:center;'>I'm Robby, an intelligent chatbot created by combining
#     the strengths of Langchain and Streamlit. I use large language models to provide
#     context-sensitive interactions. My goal is to help you better understand your data.
#     I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
#     """,
#     unsafe_allow_html=True)
# st.markdown("---")
#
#
# #Robby's Pages
# st.subheader("🚀 Robby's Pages")
# st.write("""
# - **Robby-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
# - **Robby-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
# - **Robby-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
# """)
# st.markdown("---")
#
#
#
#
#
#
#
