from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
import os
import streamlit as st
os.environ['Google_API_Key']='AIzaSyAXgoiFtqArrLaHI4nTdnITNCWQrR2V1aY'
tweet_template="Give me {number} tweets on {topic}"
tweet_prompt=PromptTemplate(template=tweet_template,input_variables=['number','topic'])
gemini_model = ChatGoogleGenerativeAI(model= "gemini-1.5-flash-latest")
tweet_generator = LLMChain(prompt = tweet_prompt, llm = gemini_model)
st.header("Tweet Generator :)")
st.subheader("Generate Tweets on any topic")
topic = st.text_input("Topic")
number=st.number_input("Number of tweets", min_value=1, max_value=10, value =1, step=1)
if st.button("Generate"):
    tweets = tweet_generator.run(number = number, topic = topic)
    st.write(tweets)
