import streamlit as st
import os
import openai
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from langchain.chat_models import ChatOpenAI




db_user = "skusr"
db_password = "shivam"
db_host = "localhost"
db_name = "employee"
os.environ['OPENAI_API_KEY'] = ""
openai.api_key = ""


llm = ChatOpenAI(model_name = 'gpt-3.5-turbo')

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
toolkit = SQLDatabaseToolkit(db = db, llm = llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    handle_parsing_errors=True
)


def rspns(txt):
    return agent_executor.run(f"{txt}")

# Set the title of the app
st.title("Chat With SQL")

# Create a text input box for the question
question = st.text_input("Enter your question:")

# Create a submit button
if st.button("Submit"):
    if question:
        # Display the entered question
        st.write("You Answer:", rspns(question))
        # You can add any processing or response generation here
    else:
        st.write("Please enter a question before submitting.")
