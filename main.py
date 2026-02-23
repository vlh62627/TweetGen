
import os
os.environ['GEMINI_API_KEY'] = st.secrets['GEMINI_API_KEY']

from langchain_google_genai import ChatGoogleGenerativeAI


from langchain_core.prompts import PromptTemplate
tweet_template = "Give me {number} tweets on {topic}"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ["number", "topic"])

gemini3 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
tweet_Chain = tweet_prompt | gemini3

import streamlit as st

st.header("Tweet EZ by VJ")

st.subheader("Generate Tweets using AI")

topic = st.text_input("Topic")

number = st.number_input("No of Tweets", min_value = 1, max_value = 10, value =1, step =1)

if st.button("Generate"):
	response = tweet_Chain.invoke({"number": number, "topic": topic})
	st.write(response.content)
