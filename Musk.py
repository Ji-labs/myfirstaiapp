from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain.prompts import PromptTemplate
import os
os.environ['Google_API_Key']='AIzaSyAXgoiFtqArrLaHI4nTdnITNCWQrR2V1aY'
tweet_template="Give me {number} tweets on {topic}"
tweet_prompt=PromptTemplate(template=tweet_template,input_variables=['number','topic'])
gemini_model = ChatGoogleGenerativeAI(model= "gemini-1.5-flash-latest")
tweet_chain = tweet_prompt | gemini_model
import streamlit as st
st.header("Tweet Generator :)")
st.subheader("Generate Tweets on any topic")
if st.button("Generate"):
  st.write("Button Pressed")
