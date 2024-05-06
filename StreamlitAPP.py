import os
import json
import pandas as pd
from dotenv import load_dotenv
from Exception.logger import logging
from Exception.exception import CustomException
import sys
from src.MCQ_GENERATOR.utils import get_table_data, read_file
import streamlit as st
# from langchain.callbacks import get_openai_callback
# from langchain.chat_models import ChatOpenAI
# from langchain_community.callbacks.manager import get_openai_callback
import langchain

import traceback
from src.MCQ_GENERATOR.MCQ_Generator import Generator



# class Module:
    
#     def __init__(self):
#         self.eval_chain = Generator.LLMChain()
#         with open("E:\ALL PROGRAMS\All_DS_Projects\Generative AI\MCQ_Gen\Response.json", 'r') as file:
#             self.Response_json = json.load(file)



#     def Streamlit_Template(self):

#         try:
#             #creating a title for the app
#             st.title("MCQs Creator Application with LangChain 🦜⛓️")

#             #Create a form using st.form
#             with st.form("user_inputs"):
#                 #File Upload
#                 uploaded_file=st.file_uploader("Uplaod a PDF or txt file")

#                 #Input Fields
#                 mcq_count=st.number_input("No. of MCQs", min_value=3, max_value=50)

#                 #Subject
#                 subject=st.text_input("Insert Subject",max_chars=20)

#                 # Quiz Tone
#                 tone=st.text_input("Complexity Level Of Questions", max_chars=20, placeholder="Simple")

#                 #Add Button
#                 button=st.form_submit_button("Create MCQs")

#                 # Check if the button is clicked and all fields have input

#                 if button and uploaded_file is not None and mcq_count and subject and tone:
#                     with st.spinner("loading..."):
#                         try:
#                             text=read_file(uploaded_file)
#                             #Count tokens and the cost of API call
#                             with get_openai_callback() as cb:
#                                 response=self.eval_chain(
#                                     {
#                                     "text": text,
#                                     "number": mcq_count,
#                                     "subject":subject,
#                                     "tone": tone,
#                                     "response_json": self.Response_json
#                                         }
#                                 )
#                             #st.write(response)

#                         except Exception as e:
#                             traceback.print_exception(type(e), e, e.__traceback__)
#                             st.error("Error")

#                         else: 
#                             print(f"Total Tokens:{cb.total_tokens}")
#                             print(f"Prompt Tokens:{cb.prompt_tokens}")
#                             print(f"Completion Tokens:{cb.completion_tokens}")
#                             print(f"Total Cost:{cb.total_cost}")
#                             if isinstance(response, dict):
#                                 #Extract the quiz data from the response
#                                 quiz=response.get("quiz", None)
#                                 if quiz is not None:
#                                     table_data=get_table_data(quiz)
#                                     if table_data is not None:
#                                         df=pd.DataFrame(table_data)
#                                         df.index=df.index+1
#                                         st.table(df)
#                                         #Display the review in atext box as well
#                                         st.text_area(label="Review", value=response["review"])
#                                     else:
#                                         st.error("Error in the table data")

#                             else:
#                                 st.write(response)
            

#         except Exception as e:
#             logging.info(f"An exception has occurred : {e}")
#             raise CustomException(e, sys) 



    