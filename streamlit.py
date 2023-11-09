# Sidebar for PDF upload and API keys
with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    customer_id = st.text_input("Vectara Customer ID", value=os.getenv("CUSTOMER_ID", ""))
    api_key = st.text_input("Vectara API Key", value=os.getenv("API_KEY", ""))
    corpus_id = st.text_input("Vectara Corpus ID", value=str(os.getenv("CORPUS_ID", "")))
    openai_api_key = st.text_input("OpenAI API Key", value=os.getenv("OPENAI_API_KEY", ""))
    submit_button = st.button("Submit")

# Constants
CUSTOMER_ID = customer_id if customer_id else os.getenv("CUSTOMER_ID")
API_KEY = api_key if api_key else os.getenv("API_KEY")
CORPUS_ID = int(corpus_id) if corpus_id else int(os.getenv("CORPUS_ID", 0))  # Assuming CORPUS_ID should be an integer
OPENAI_API_KEY = openai_api_key if openai_api_key else os.getenv("OPENAI_API_KEY")